from dotenv import load_dotenv, find_dotenv
from datetime import datetime
import os
import requests
import smtplib

load_dotenv(find_dotenv())

MY_LAT = -15.821760 # Your latitude
MY_LONG = -48.113480 # Your longitude
FROM_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")

def check_position(
    user_position: tuple[float, float],
    iss_position: tuple[float, float]
) -> bool:
    """Return true if the margin of error between the user's location and the iss location is less than 5 degrees."""

    x_error = abs(iss_position[0] - user_position[0])
    y_error = abs(iss_position[1] - user_position[1])

    if x_error <= 5 and y_error <= 5:
        return True

    return False


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
is_near = check_position((MY_LAT, MY_LONG), (iss_latitude, iss_longitude))

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

if is_near:

    with smtplib.SMTP() as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"""Subject:The ISS is right over your head!\n\n
            It's {hour_now}h, so if it's dark enough in your location, you might see it in the sky."""
        )

else:

    print("The ISS is not over your head yet.")



