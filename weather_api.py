import requests
import os

def get_weather_forecast(lat, lon):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    return res["list"][:5]
