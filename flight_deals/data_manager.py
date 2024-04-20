import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
USERS_ENDPOINT = os.environ.get("USERS_ENDPOINT")

class DataManager:
    def __init__(self) -> None:
        self.destination_data = []

    def get_destination_data(self) -> list[dict]:
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

    def get_users(self) -> list[dict]:
        response = requests.get(url=USERS_ENDPOINT)
        response.raise_for_status()

        users = response.json()["users"]
        return users
