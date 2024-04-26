import os
import smtplib
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

USER = os.environ.get("FROM_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

class NotificationManager:
    def __init__(self) -> None:
        pass

    def send_mail(self, price: float) -> None:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(
                from_addr=USER,
                to_addrs=TO_EMAIL,
                msg=f"Subject:Low Price\n\nHey, the product you were looking for is R${price} right now. It's time to buy it!")

