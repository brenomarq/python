import os
import requests
from dotenv import load_dotenv, find_dotenv
from twilio.rest import Client

load_dotenv(find_dotenv())

def get_stock_prices(stock_name: str, apikey: str) -> list[float]:
    """Given a stock name and an apikey, it returns a list with the two latest closing prices for the
    specified stock."""

    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_name,
        "apikey": apikey,
    }

    response = requests.get(url=url, params=params)
    response.raise_for_status()

    data: dict = response.json()['Time Series (Daily)']
    data_list = [value for value in data.values()]
    yesterday_closing_price = float(data_list[0]['4. close'])
    otherday_closing_price = float(data_list[1]['4. close'])

    return [yesterday_closing_price, otherday_closing_price]


def get_news(
        topic: str,
        apikey: str
    ) -> list[dict]:
    """Given a topic and an apikey, it returns a list with 3 main news about the specified topic"""

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "apiKey": apikey,
        "language": "en",
    }

    response = requests.get(url=url, params=params)
    response.raise_for_status()

    articles: list[dict] = response.json()['articles'][:3]
    desired_articles = [
        {
            "title": news.get("title"),
            "description": news.get("description")
        }
        for news in articles
    ]

    return desired_articles


def check_percentage(
        first_price: float,
        other_price: float
    ) -> list[bool, str]:
    """Get two stock prices as inputs and return a list in which the first item is a boolean telling if the percentage
    is greater than 5 and a formatted message."""

    is_great = False
    msg = None

    difference = first_price - other_price
    diff_percent = (difference / first_price) * 100
    if diff_percent < 0:
        msg = f"🔻 {(diff_percent)*(-1):.2f}%"

    else:
        msg = f"🔺 {diff_percent:.2f}%"

    return [is_great, msg]


def send_sms(
        client: Client,
        message: str
    ) -> None:
    """Sends an SMS message to myself with twilio API."""

    msg = client.messages.create(
        to=os.environ.get("MY_PHONE"),
        from_=os.environ.get("TWILIO_PHONE"),
        body=message
    )

    print(msg.status)
