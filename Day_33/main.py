import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 52.399448 # Your latitude
MY_LONG = 0.259790 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

def is_the_iss_near(my_lat, my_lng, i_lat, i_lng):
    return abs(my_lat - i_lat) <= 5 and abs(my_lng - i_lng) <= 5

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

def is_it_dark(rise, set, hour):
    return hour >= set or hour <= rise

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# current_time = 0
# TARGET_TIME = 60

# def countdown():
#     global current_time

#     current_time += 1
#     if current_time % TARGET_TIME == 0:
#         return True
#     return False

while True:
    time.sleep(60)
    if is_it_dark(sunrise, sunset, time_now.hour) and is_the_iss_near(MY_LAT, MY_LONG, iss_latitude, iss_longitude):
        email = "pierstheprogrammer@gmail.com"
        password = "fkkf blby pieq nbra"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
                email, 
                "piers.taylorr@gmail.com", 
                msg=f"Subject:ISS above!\n\nThe iss is right above. Look up!".encode("utf-8")
            )
    
