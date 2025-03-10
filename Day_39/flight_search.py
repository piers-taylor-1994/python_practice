import requests
import os
from dotenv import load_dotenv
from datetime import *

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.base_url = "https://test.api.amadeus.com"
        self.headers = {
            "Authorization": self.get_access_token(),
            "accept": "application/vnd.amadeus+json"
        }
        self.origin_code = "LON"

    def get_access_token(self):
        response = requests.post(
            f"{self.base_url}/v1/security/oauth2/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                f"grant_type":"client_credentials",
                "client_id":{os.environ["AMADEUS_API_KEY"]},
                "client_secret": {os.environ["AMADEUS_API_SECRET"]}
            }
        )
        response.raise_for_status()
        return f"Bearer {response.json()["access_token"]}"
    
    def get_city_code(self, city):
        response = requests.get(
            f"{self.base_url}/v1/reference-data/locations/cities",
            headers=self.headers,
            params={
                "keyword": city.upper(),
                "max": "1",
                "include": "AIRPORTS"
            }
        )
        response.raise_for_status()
        return response.json()["data"][0]["iataCode"]
    
    def get_flight_offers(self, destination_code):
        response = requests.get(
            f"{self.base_url}/v2/shopping/flight-offers",
            headers=self.headers,
            params={
                "originLocationCode": self.origin_code,
                "destinationLocationCode": destination_code,
                "departureDate": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
                "returnDate": (datetime.now() + timedelta(weeks=(4 * 6))).strftime("%Y-%m-%d"),
                "adults": 1,
                "currencyCode": "GBP",
                "max": 10
            }
        )
        response.raise_for_status()
        return response.json()