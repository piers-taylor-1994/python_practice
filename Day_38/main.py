import requests
from datetime import *
import os
from dotenv import load_dotenv

load_dotenv()

nutrition_headers = {
    "x-app-id": os.environ["X-APP-ID"],
    "x-app-key": os.environ["X-APP-KEY"],
}

nutrition_params = {
    "query": input("Tell me which exercises you did: ")
}

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", headers=nutrition_headers, json=nutrition_params)
response.raise_for_status()
exercises = response.json()["exercises"]

date_now = datetime.now()

sheety_headers = {
    "Authorization": os.environ["AUTHORIZATION"]
}

for exercise in exercises:
    sheety_params = {
        "workout": {
            "date": date_now.strftime("%d/%m/%Y"),
            "time": date_now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post("https://api.sheety.co/b551df358b844170fcbe21bf469b2f5e/workoutTracking/workouts", headers=sheety_headers, json=sheety_params)
    print(sheety_response.json())