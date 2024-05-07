import os
from dotenv import load_dotenv, find_dotenv
from twitterbot import InternetComplaintTwitterBot
load_dotenv(find_dotenv())

SPEED_URL = "https://www.speedtest.net/"
TWITTER_EMAIL = os.environ.get("EMAIL")
TWITTER_PASSWORD = os.environ.get("PASSWORD")
PROMISED_DOWNLOAD = 150.0
PROMISED_UPLOAD = 50.0

twitter_bot = InternetComplaintTwitterBot()

is_slow = twitter_bot.is_internet_slow(url=SPEED_URL, speeds=[PROMISED_DOWNLOAD, PROMISED_UPLOAD])

if is_slow:
    print("The internet is slow.")

    twitter_bot.twitter_login(
        email=TWITTER_EMAIL,
        password=TWITTER_PASSWORD,
        user="brenomp516"
    )

    twitter_bot.send_tweet()
