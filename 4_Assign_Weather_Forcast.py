import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# Create a session with caching and retry capabilities
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Function to get weather data for a city
def get_weather(city):
    # You can use a service like Geonames to get the latitude and longitude of a city based on its name.
    # For simplicity, I'll hardcode coordinates for Berlin, Germany here.
    latitude = 52.52
    longitude = 13.41

    # Define the API URL and parameters for temperature
    temperature_url = "https://api.open-meteo.com/v1/forecast"
    temperature_params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
    }

    # Get temperature data
    temperature_responses = openmeteo.weather_api(temperature_url, params=temperature_params)
    temperature_response = temperature_responses[0]

    # Define the API URL and parameters for weather description
    description_url = "https://api.open-meteo.com/v1/forecast"
    description_params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "weathercode",
    }

    # Get weather description data
    description_responses = openmeteo.weather_api(description_url, params=description_params)
    description_response = description_responses[0]

    # Define the API URL and parameters for humidity
    humidity_url = "https://api.open-meteo.com/v1/forecast"
    humidity_params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "humidity_2m",
    }

    # Get humidity data
    humidity_responses = openmeteo.weather_api(humidity_url, params=humidity_params)
    humidity_response = humidity_responses[0]

    return temperature_response, description_response, humidity_response

# Function to display weather information
def display_weather(temperature_response, description_response, humidity_response):
    temperature = temperature_response.Hourly().Variables(0).ValuesAsNumpy()[-1]  # Get the latest temperature
    description = description_response.Hourly().Variables(0).ValuesAsNumpy()[-1]  # Get the latest weather description code
    humidity = humidity_response.Hourly().Variables(0).ValuesAsNumpy()[-1]  # Get the latest humidity

    print(f"Temperature: {temperature}°C")
    print(f"Description Code: {description}")
    print(f"Humidity: {humidity}%")

# Main program
if __name__ == "__main__":
    city = input("Enter the city name: ")
    temperature_response, description_response, humidity_response = get_weather(city)

    if temperature_response and description_response and humidity_response:
        display_weather(temperature_response, description_response, humidity_response)
    else:
        print("Weather data not available for the specified city.")
