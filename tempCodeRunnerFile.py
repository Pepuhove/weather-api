import requests
import json
API_KEYS = "afdd44f7a8a40efc53bed09a3582e670"
CITY = "Cape Town"
response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEYS}&q={CITY}")

print(response.status_code)
if response.status_code == 200:
    print("Weather data retrieved successfully")
    weather_data = response.json()
    print(json.dumps(weather_data, indent=4))
else:
    print("Failed to retrieve weather data")
    print(f"Error: {response.status_code} - {response.text}")