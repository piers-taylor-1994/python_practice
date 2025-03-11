import os
import requests
from dotenv import load_dotenv
import smtplib

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self.smtp_address = os.environ["SMTP_ADDRESS"]
        self.email_address_from = os.environ["EMAIL_ADDRESS_FROM"]
        self.email_password = os.environ["EMAIL_PASSWORD"]
        self.headers = {
            "Authorization": os.environ["SHEETY_TOKEN"]
        }
        self.destination_data = {}
        self.users_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.prices_endpoint, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # print(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(
            self.users_endpoint,
            headers=self.headers
        )
        response.raise_for_status()
        data = response.json()
        self.users_data = data["users"]

        return self.users_data
    
    def send_emails(self, message):
        self.get_customer_emails()

        for user in self.users_data:
            print(f"Sending email to {user["whatIsYourEmail?"]}")
            with smtplib.SMTP(self.smtp_address, port=587) as connection:
                connection.starttls()
                result = connection.login(self.email_address_from, self.email_password)
                connection.sendmail(
                    from_addr=self.email_address_from,
                    to_addrs=user["whatIsYourEmail?"],
                    msg=f"Subject:Flight alert!\n\n{message}".encode("utf-8")
                )
