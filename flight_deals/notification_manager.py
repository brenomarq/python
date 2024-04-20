import os
import smtplib
from dotenv import load_dotenv, find_dotenv
from flight_data import FlightData
from twilio.rest import Client
load_dotenv(find_dotenv())

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
TOKEN = os.environ.get("TOKEN")
FROM_NUMBER = os.environ.get("FROM_NUMBER")
TO_NUMBER = os.environ.get("TO_NUMBER")

FROM_EMAIL = os.environ.get("FROM_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

class NotificationManager:
    def __init__(self) -> None:
        self.client = Client(ACCOUNT_SID, TOKEN)

    def send_alert(self, flight_data: FlightData):
        message = self.client.messages.create(
            body=f"Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}.",
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )

        print(message.status)

    def send_email(self, email: str, flight_data: FlightData) -> None:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=FROM_EMAIL, to_addrs=email, msg=f"Subject: Cheap Flight!\n\nLow price alert! Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}.\n\nFlight has {flight_data.step_overs} stop over, via {flight_data.via_city}.")
