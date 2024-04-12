import os
from dotenv import load_dotenv, find_dotenv
from functions import check_percentage, get_stock_prices, get_news, send_sms
from twilio.rest import Client

# Load Environment Variables
load_dotenv(find_dotenv())

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

prices = get_stock_prices(
    stock_name=STOCK,
    apikey=os.environ.get("STOCK_API_KEY")
)

info = check_percentage(
    first_price=prices[0],
    other_price=prices[1]
)

shall_get_news = info[0]
msg = info[1]

if shall_get_news:
    articles = get_news(
        topic=COMPANY_NAME,
        apikey=os.environ.get("NEWS_API_KEY")
    )

    twilio_client = Client(os.environ.get("ACCOUNT_SID"), os.environ.get("AUTH_TOKEN"))

    for article in articles:
        formatted_msg = f"""{msg},\n
        Headline: {article['title']}\n
        Brief: {article['description']}"""

        send_sms(
            client=twilio_client,
            message=formatted_msg
        )

else:
    print("Not a great variation today")

