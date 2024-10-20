# utils/visualizations.py

import sqlite3
import matplotlib.pyplot as plt

def plot_daily_summary():
    conn = sqlite3.connect("data/weather_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, avg_temp, max_temp, min_temp FROM daily_summary")
    data = cursor.fetchall()
    conn.close()

    dates, avg_temps, max_temps, min_temps = zip(*data)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, label='Avg Temp', marker='o')
    plt.plot(dates, max_temps, label='Max Temp', marker='o')
    plt.plot(dates, min_temps, label='Min Temp', marker='o')
    plt.title('Daily Weather Summary')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
