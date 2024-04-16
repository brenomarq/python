import datetime
import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

APP_ID = os.environ.get("NUTRI_ID")
API_KEY = os.environ.get("NUTRI_KEY")
TOKEN = os.environ.get("TOKEN")

exercises = input("Tell me what you did today: ")

# Get information about the exercises done today
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_body = {
    "query": exercises,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=nutri_endpoint, json=nutri_body, headers=headers)
response.raise_for_status()

workout_data: list[dict] = response.json()["exercises"]

# Prepare to send the data to Google Sheets
sheety_endpoint = os.environ.get("SHEET_ENDPOINT")

today = datetime.datetime.now()
for exercise in workout_data:
    name: str = exercise["name"].title()
    duration: float = exercise["duration_min"]
    calories: float = exercise["nf_calories"]

    sheety_body = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": name,
            "duration": duration,
            "calories": calories,
        }
    }

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url=sheety_endpoint, json=sheety_body, headers=headers)
    response.raise_for_status()

    print(response.text)
