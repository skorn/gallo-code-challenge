## Expectations

The following code challenge is meant to be an open-ended yet straightforward exercise for you to demonstrate your capabilities with backend development. This absolutely does not need to be a polished product. What we're looking for is how you approach the problem, use best practices, and leverage your experience to create solutions efficiently. There's no need to spend more than a couple hours on this challenge; we'll review everything you submit and give you a chance to explain your work.

We're excited to see what you create!

## Prerequisites

- Access to an IDE
- Knowledge of Python or JavaScript Programming
- Use git to checkout and submit your code

## Goals

1. Store data.json in a database
2. Create an API endpoint to return a list of locations provided in data.json
3. Create an API endpoint to return weather data for a requested record in data.json

#### Details

The provided file data.json contains a few of our fields in California.
The data is standard JSON format and should be familiar to you,
but our geographic points conform to a specific format called GeoJSON.
You don't need to know a lot about GeoJSON other than coordinates will be stored like this:

```
{
    geometry: {
        type: Point,
        coordinates: [<longitude>, <latitude>]
    }
}
```

If you'd like to read more about GeoJSON you can find the spec here: <https://geojson.org/>

You can find current weather conditions through an API called _OpenWeatherMap_.  

Please create a free account and use their API to fetch weather data. You are welcome to store static weather data in your DB, but using CORS to fetch current weather conditions would be a bonus.

<https://openweathermap.org/api>

Please create a public GitHub repo and host your code there.


## Stretch Goal: Front End Expertise

If you'd like to demonstrate additional skills we've added an optional goal below. This is purely optional: don't feel like you have to spend a lot of time on this. Even if you don't finish we'll be happy to look at any progress you've made.

#### Details

Create a presentation layer for the data you are returning from your API. This can be a web app, iOS app, static file, or any other method for communicating with an end user.

