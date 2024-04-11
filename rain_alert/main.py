import os
import requests
from dotenv import load_dotenv, find_dotenv
from twilio.rest import Client

# Enviroment Variables
load_dotenv(find_dotenv())

# Twilio settings
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_number = os.environ.get("MY_PHONE")
twilio_number = os.environ.get("TWILIO_PHONE")

# Open Weather API settings
URL = "https://api.openweathermap.org/data/2.5/forecast"
LAT = -15.826691
LNG = -47.921822
API_KEY = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat": LAT,
    "lon": LNG,
    "units": "metric",
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(url=URL, params=weather_params)
response.raise_for_status()

will_rain = False
data: list[dict] = response.json()["list"]
for item in data:
    weather_id: int = item['weather'][0]['id']

    if weather_id < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today! Do not forget to bring an ☔.",
        from_=twilio_number,
        to=my_number
    )

    print(message.status)
