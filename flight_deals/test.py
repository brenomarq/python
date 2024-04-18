import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

endpoint = "https://api.tequila.kiwi.com/v2/search"

headers = {
    "apikey": os.environ.get("TEQUILA_KEY")
}

params = {
    "fly_from": "LON",
    "fly_to": "NYC",
    "date_from": "19/04/2024",
    "date_to": "19/08/2024",
    "curr": "GBP",
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
}

response = requests.get(url=endpoint, params=params, headers=headers)
response.raise_for_status()

flight_price = response.json()["data"][0]["price"]
print(flight_price)

