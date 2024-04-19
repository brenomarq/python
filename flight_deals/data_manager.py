import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

class DataManager:
    def __init__(self) -> None:
        self.destination_data = {}

    def get_destination_data(self) -> None:
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()

        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_code(self, codes: dict[str]) -> None:
        for row in self.destination_data:
            id: int = row["id"]
            code = codes.get(id)

            if code:
                endpoint = f"{SHEETY_ENDPOINT}/{row['id']}"

                body = {
                    "price": {
                        "iataCode": code,
                    }
                }

                response = requests.put(url=endpoint, json=body)
                response.raise_for_status()

                print(response.text)

#     def update_destination_codes(self):
#         for city in self.destination_data:
#             new_data = {
#                 "price": {
#                     "iataCode": city["iataCode"]
#                 }
#             }
#             response = requests.put(
#                 url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
#                 json=new_data
#             )
#             print(response.text)
