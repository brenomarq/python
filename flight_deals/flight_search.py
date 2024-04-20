import os
import requests
from dotenv import load_dotenv, find_dotenv
from flight_data import FlightData
load_dotenv(find_dotenv())

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TEQUILA_KEY")

class FlightSearch:
    def __init__(self) -> None:
        pass

    def get_destination_code(self, city_name: str) -> str:
        endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey": TEQUILA_API_KEY,
        }
        params = {
            "term": city_name,
            "location_types": "city",
        }

        response = requests.get(url=endpoint, params=params, headers=headers)
        response.raise_for_status()

        result = response.json()["locations"]
        code = result[0]["code"]
        return code

    def check_flights(
            self,
            origin_code: str,
            destination_code: str,
            from_time: str,
            to_time: str
    ) -> FlightData:
        endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": from_time,
            "date_to": to_time,
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stop_overs": 0,
        }

        response = requests.get(url=endpoint, headers=headers, params=params)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            params["max_stop_overs"] = 1

            response = requests.get(url=endpoint, headers=headers, params=params)
            response.raise_for_status()

            data = response.json()["data"][0]

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )

            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
