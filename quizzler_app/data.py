import requests

URL = "https://opentdb.com/api.php"
params = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(URL, params=params)
data = response.json()
question_data = data["results"]
