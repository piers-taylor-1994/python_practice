class NotificationManager:
    def __init__(self):
        self.base_url = ""
        self.token = ""
        self.api_key = ""
        self.api_secret = ""

    def send_notification(self, flight_info):
        notification = f"Sent from your Twilio trial account - Low price alert! Only £{flight_info.price} "
        notification += f"to fly from {flight_info.home_airport_code} to {flight_info.destination_airport_code}, "
        notification += f"on {flight_info.from_date} until {flight_info.to_date}."
        return notification