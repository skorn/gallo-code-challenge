FROM python:3.8

WORKDIR /opt/app

ARG openweather_api_key # you could give this a default value as well
ENV APP_openweather_api_key=$openweather_api_key

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
