from data_manager import *
from flight_search import *
from flight_data import find_cheapest_flight
from notification_manager import *
import time

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

#---------------Update google sheet IATA codes---------------#
# for destination in data_manager.destinations:
#     destination["iataCode"] = flight_search.get_city_code(destination["city"])
# data_manager.update_row()

for destination in data_manager.destinations:
    cheapest_flight = find_cheapest_flight(flight_search.get_flight_offers(destination["iataCode"]))
    print(f"Cheapest flight for {destination["city"]} = £{cheapest_flight.price}")
    if cheapest_flight.price != "N/A" and float(destination["lowestPrice"]) > float(cheapest_flight.price):
        print(notification_manager.send_notification(cheapest_flight))
    time.sleep(1)