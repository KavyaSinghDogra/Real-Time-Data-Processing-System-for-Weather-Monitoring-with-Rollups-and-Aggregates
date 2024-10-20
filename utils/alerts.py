# utils/alerts.py

def check_alerts(weather_data):
    temperature = weather_data['main']['temp']
    city = weather_data['name']
    if temperature > 35:
        print(f"Alert! High temperature in {city}: {temperature}°C")
