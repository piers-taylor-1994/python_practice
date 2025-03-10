class FlightData:

    def __init__(self, price, home_code, destination_code, from_date, to_date):
        self.price = price
        self.home_airport_code = home_code
        self.destination_airport_code = destination_code
        self.from_date = from_date
        self.to_date = to_date

def find_cheapest_flight(data):
    flight_data = data["data"]
    cheapest_flight = FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    if len(flight_data) > 0:
        cheapest_flight = FlightData(
            flight_data[0]["price"]["grandTotal"],
            flight_data[0]["itineraries"][0]["segments"][0]["departure"]["iataCode"],
            flight_data[0]["itineraries"][1]["segments"][0]["departure"]["iataCode"],
            flight_data[0]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
            flight_data[0]["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
        )
    for flight in flight_data[1:]:
        if flight["price"]["grandTotal"] < cheapest_flight.price:
            cheapest_flight = FlightData(
                flight[0]["price"]["grandTotal"],
                flight[0]["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                flight[0]["itineraries"][1]["segments"][0]["departure"]["iataCode"],
                flight[0]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
                flight[0]["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            )
    return cheapest_flight