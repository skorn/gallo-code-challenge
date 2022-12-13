#!/usr/bin/env bash

if [[ $openweather_api_key =~ ^[0-9a-zA-Z] ]]; then
    docker container prune -f
    docker build -t gallo-code-challenge --build-arg openweather_api_key .
    docker run -it -p 8080:8080 gallo-code-challenge
else
    echo 'Please provide api key for openweather with: export openweather_api_key="ABCD"'
    exit 1
fi

