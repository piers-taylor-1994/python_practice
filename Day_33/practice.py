import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# print(data)

response = requests.get("https://api.sunrise-sunset.org/json", {"lat": 52.399448, "lng": 0.259790, "formatted": 0})
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
print(sunrise.split("T")[1].split(":")[0])