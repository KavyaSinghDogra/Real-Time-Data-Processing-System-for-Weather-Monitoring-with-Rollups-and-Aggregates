# main.py

import time
from config.config import METRO_CITIES, INTERVAL
from utils.api_helper import get_weather_data
from utils.database_helper import store_daily_summary
from utils.alerts import check_alerts

def process_weather_data(weather_data):
    """
    Process the weather data to create a daily summary.
    """
    date = time.strftime('%Y-%m-%d', time.localtime(weather_data['dt']))
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']

    daily_summary = {
        'date': date,
        'avg_temp': temp,
        'max_temp': temp,
        'min_temp': temp,
        'dominant_condition': weather_data['weather'][0]['main']
    }

    return daily_summary

def main():
    while True:
        for city in METRO_CITIES:
            weather_data = get_weather_data(city)
            if weather_data:
                daily_summary = process_weather_data(weather_data)
                store_daily_summary(daily_summary)
                check_alerts(weather_data)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
