# utils/api_helper.py

import requests
from config.config import BASE_URL, API_KEY

def get_weather_data(city):
    response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {city}: {response.status_code}")
        return None
