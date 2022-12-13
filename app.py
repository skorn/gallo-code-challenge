from flask import Flask, render_template, request
from sqlite_utils import Database
import os
import json
import requests


#############################################################
# Define some required variables for reaching openweather
#############################################################
api_path = "/api/v1"
openweather_api_key = os.environ.get('APP_openweather_api_key')
openweather_api_path = f"https://api.openweathermap.org/data/3.0/onecall?appid={openweather_api_key}&exclude=hourly,daily"


#############################################################
#############################################################
# Helper functions
#############################################################
#############################################################

#############################################################
# Initialize DB with data provided
#############################################################
def setup_db():
    db = Database('database.db')
    with open('schema.sql') as schema_file:
        db.executescript(schema_file.read())
    data_file = open('data.json')
    data_json = json.load(data_file)
    for region in data_json:
        for entry in data_json[region]:
            db["locations"].insert({"region": region, "name": entry["name"], "coordinates": entry["geometry"]["coordinates"]})
    db.close()

#############################################################
# Handler to initilize connection
#############################################################
def get_db_connection():
    db = Database('database.db')
    return db

#############################################################
# Validate that db is initialized and data is present
#############################################################
def validate_db(db):
    tables = db.table_names()
    if 'locations' in tables: return True
    return False

#############################################################
# Format response based on whether html or json was requested
#############################################################
def format_response(header, response, title):
    if "text/html" in header:
        body = json.dumps(response, indent=8).replace('\n', "<br />").replace("        ", "&nbsp;&nbsp;&nbsp;&nbsp;")
        return f"<font size=\"5\">{title}:</font><br />{body}"
    return response


#############################################################
#############################################################
# Flask configuration
#############################################################
#############################################################
setup_db() # First time setup before flask starts to populate data
app = Flask(__name__)

#############################################################
# Endpoint to list all regions
#############################################################
@app.route(api_path + '/regions')
def regions():
    db = get_db_connection()
    result = db.execute('SELECT DISTINCT region FROM locations').fetchall()
    if 'request' in globals():
        return format_response(request.headers.get("Accept"), result, "Regions2:")
    return result

#############################################################
# Endpoint to list locations in specific region
#############################################################
@app.route(api_path + '/region/<region>')
def region(region):
    db = get_db_connection()
    result = db.execute('SELECT name FROM locations WHERE region == ?', [region.capitalize()]).fetchall()
    if 'request' in globals():
        return format_response(request.headers.get("Accept"), result, "Region:")
    return result

#############################################################
# Endpoint to list all locations
#############################################################
@app.route(api_path + '/locations')
def locations():
    db = get_db_connection()
    if validate_db(db):
        result = db.execute('SELECT region, name FROM locations').fetchall()
        db.close()
        if 'request' in globals():
            return format_response(request.headers.get("Accept"), result, "Locations:")
        return result
    else:
        return "Table not found, perhaps you need to load /ingest first"

#############################################################
# Endpoint to list information on specific location
#############################################################
@app.route(api_path + '/location/<location>')
def location(location):
    db = get_db_connection()
    if validate_db(db):
        result = db.execute('SELECT region, name, coordinates FROM locations WHERE name == ?', [location.upper()]).fetchall()
        db.close()
        if 'request' in globals():
            return format_response(request.headers.get("Accept"), result, "Location:")
        return result
    else:
        return "Table not found, perhaps you need to load /ingest first"

#############################################################
# Endpoint to get weather info on specific location
#############################################################
@app.route(api_path + '/location/<location>/weather')
def weather(location):
    db = get_db_connection()
    if validate_db(db):
        db_result = db.execute('SELECT coordinates, region FROM locations WHERE name == ?', [location.upper()]).fetchall()
        db.close()
        longitude = json.loads(db_result[0][0])[0]
        latitude = json.loads(db_result[0][0])[1]
        response = requests.get(f"{openweather_api_path}&lat={latitude}&lon={longitude}").json()
        payload = {
                "region": db_result[0][1],
                "name": location.upper(),upper,
                "coordinates": db_result[0][0],
                "current_weather": json.loads(response)["current"],
                }
        del payload["current"]["id"]
        del payload["current"]["icon"]
        if 'request' in globals():
            return format_response(request.headers.get("Accept"), payload, "Weather Data:")
        return response
    else:
        return "Table not found, perhaps you need to load /ingest first"
