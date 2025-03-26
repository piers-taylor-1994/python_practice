import requests
import os
from twilio.rest import Client

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Rain',
  to='whatsapp:+447906533604'
)

params = {
    "lat": 52.399448, 
    "lon": 0.259790, 
    "appid": WEATHER_API_KEY,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params)
response.raise_for_status()
weather_data = response.json()["list"]
# for weather_dict in weather_data:
#     if weather_dict["weather"][0]["id"] < 700:
#         print("Bring an umbrella")
#         break
if any([int(weather_instance["weather"][0]["id"]) < 700 for weather_instance in weather_data]):
  message = client.messages.create(
  from_='whatsapp:+14155238886',
  body="It's going to rain today. Remember to bring an umbrella!",
  to='whatsapp:+447906533604'
  )
  print(message.status)