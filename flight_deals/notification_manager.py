import os
from dotenv import load_dotenv, find_dotenv
from flight_data import FlightData
from twilio.rest import Client
load_dotenv(find_dotenv())

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
TOKEN = os.environ.get("TOKEN")
FROM_NUMBER = os.environ.get("FROM_NUMBER")
TO_NUMBER = os.environ.get("TO_NUMBER")

class NotificationManager:
    def __init__(self) -> None:
        self.client = Client(ACCOUNT_SID, TOKEN)

    def send_alert(self, flight_data: FlightData):
        message = self.client.messages.create(
            body=f"Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}.",
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )
