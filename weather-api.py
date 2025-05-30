import os
import requests
import time
import json
from dotenv import load_dotenv

def is_valid_city_name(city):
    return city.replace(" ", "").isalpha()  # allows multi-word city names

def get_weather(city):
    load_dotenv()
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        print("Error: WEATHER_API_KEY not found in environment variables.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("\nFetching data from OpenWeatherAPI...\n")
            time.sleep(3)
            print(f"\nWeather data retrieved successfully for the city of {city_name}:\n")
            weather_data = response.json()
            print(json.dumps(weather_data, indent=4))
        else:
            print("\nFailed to retrieve weather data.")
            print(f"Error: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    while True:
        city_name = input("Enter a city name: ").strip()
        if is_valid_city_name(city_name):
            get_weather(city_name.lower())
            break
        else:
            print("❌ Invalid input. Please enter a valid city name (letters only).")
