"""
TASK 3 . HARD
Real API + Analysis
Use the Open-Meteo weather API (free, no key needed) to fetch 7-day weather forecast for Lalitpur. Save to CSV. Find the hottest and coldest day.
Steps:
API: https://api.open-meteo.com/v1/forecast
Params: Lalitpur's latitude, longitude, daily=temperature_2m_max
Save: date + max_temp to  weather.csv
Find max/min temp and print which day
Bonus: save a summary to a .txt file
Deliverable: weather.csv + analysis script + summary.txt
"""

import requests
import csv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("WEATHER_API_URL")

if not url:
    raise ValueError("WEATHER_API_URL not found in .env")

# API parameters
params = {
    "latitude": 27.6728,          # Lalitpur
    "longitude": 85.3188,
    "daily": "temperature_2m_max"
}

try:
    response = requests.get(url, params=params)

    print("Weather data fetched successfully.")

    data = response.json()
    daily = data.get("daily", {})

    dates = daily.get("time", [])
    temps = daily.get("temperature_2m_max", [])

    # Save to CSV
    with open("weather.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Date", "Max Temperature"])
        writer.writeheader()

        for date, temp in zip(dates, temps):
            writer.writerow({
                "Date": date,
                "Max Temperature": temp
            })

    print(f"Saved {len(dates)} records to weather.csv")

    # Analysis 
    hottest_day, max_temp = max(zip(dates, temps), key=lambda x: x[1])
    coldest_day, min_temp = min(zip(dates, temps), key=lambda x: x[1])

    # Save summary
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write("Weather Summary for Lalitpur\n")
        f.write(f"Latitude: {params['latitude']}, Longitude: {params['longitude']}\n\n")

        f.write(f"Hottest day: {hottest_day} ({max_temp}°C)\n")
        f.write(f"Coldest day: {coldest_day} ({min_temp}°C)\n\n")

        f.write("7-Day Temperature Forecast:\n")
        for date, temp in zip(dates, temps):
            f.write(f"{date} -> {temp}°C\n")

    print("Summary saved to summary.txt")


except Exception as e:
    print(f"Error: {e}")