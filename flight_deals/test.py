import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

ENDPOINT = os.environ.get("USERS_ENDPOINT")

response = requests.get(url=ENDPOINT)
response.raise_for_status()

print(response.text)
