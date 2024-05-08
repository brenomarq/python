import os
import time
from instagrambot import InstagramBot
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

INSTA_EMAIL = os.environ.get("EMAIL")
INSTA_PASSWORD = os.environ.get("PASSWORD")

bot = InstagramBot()
bot.login(user=INSTA_EMAIL, password=INSTA_PASSWORD)
