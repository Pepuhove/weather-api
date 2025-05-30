🌤️ **Weather API CLI Tool**

A simple Python command-line tool that fetches and displays real-time weather 
data for a user-specified city using the OpenWeatherMap API.

🔧 **Features**

Retrieves current weather information via OpenWeatherMap API

Input validation to ensure only valid city names are accepted

Graceful error handling for failed API calls and invalid inputs

Environment variable support to keep API keys secure using .env


🛠️ **Technologies Used**

Python 3.x

requests for HTTP requests

dotenv for secure API key management

OpenWeatherMap API


🚀 **How to Run**

Clone the Repository


git clone https://github.com/Pepuhove/weather-api-cli.git

cd weather-api-cli
Install Dependencies


pip install -r requirements.txt
Set Up Environment Variables

Create a .env file in the root directory with your API key:


WEATHER_API_KEY=your_openweathermap_api_key
Run the Script

python weather.py


📦 **Example Usage**

css


Enter a city name: London

Weather data retrieved successfully:

{

  "coord": {...},
  
  "weather": [...],
  
  "main": {
  
    "temp": 285.3,
    
    ...
    
  },
  
  ...
  
}


⚠️ **Error Handling**


Invalid input (e.g., numbers or empty string) prompts user again

Displays clear error messages for HTTP issues or missing API key


📄 **License**

This project is open-source and available under the MIT License.
