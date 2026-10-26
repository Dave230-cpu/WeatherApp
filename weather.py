
import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 50.0755,
    "longitude": 14.4378,
    "current": "temperature_2m",
    "timezone": "Europe/Prague"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())
