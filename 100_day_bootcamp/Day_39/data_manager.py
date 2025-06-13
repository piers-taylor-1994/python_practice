import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.base_url = "https://api.sheety.co/b551df358b844170fcbe21bf469b2f5e/flightDeals/prices"
        self.headers = {
            "Authorization": os.environ["SHEETY_TOKEN"]
        }
        self.destinations = self.get_rows()
    
    def get_rows(self):
        response = requests.get(
            self.base_url,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()["prices"]
    
    def update_row(self):
        for destination in self.destinations:
            response = requests.put(
                f"{self.base_url}/{destination["id"]}",
                headers=self.headers,
                json={
                    "price": {
                        "iataCode": destination["iataCode"],
                    }
                }
            )
            response.raise_for_status()
            print(response.json())