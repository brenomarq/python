import os
import requests
from datetime import datetime
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER = "breno516"
GRAPH_ID = "graph1"

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "30",
}

headers = {
    "X-USER-TOKEN": os.environ.get("TOKEN")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
