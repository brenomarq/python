from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_IATA = "LON"

sheet_data = data_manager.get_destination_data()

codes = {}
for row in sheet_data:
    if not row["iataCode"]:
        id: int = row["id"]
        city: str = row["city"]

        code = flight_search.get_destination_code(city_name=city)
        codes[id] = code

if len(codes) > 0:
    data_manager.update_destination_code(codes)

tomorrow = datetime.now() + timedelta(days=1)
six_months_ahead = datetime.now() + timedelta(days=6*30)

flights = []
for row in sheet_data:
    flight = flight_search.check_flights(
        origin_code=ORIGIN_IATA,
        destination_code=row["iataCode"],
        from_time=tomorrow.strftime("%d/%m/%Y"),
        to_time=six_months_ahead.strftime("%d/%m/%Y")
    )

    flights.append(flight)


for index, row in enumerate(sheet_data):
    flight_data = flights[index]

    if flight_data.price < row["lowestPrice"]:
        notification_manager.send_alert(flight_data)
