import os
import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 182
AGE = 22

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get("TOKEN")
EXERCISE_ENDPOINT = os.environ.get("EXERCISE_ENDPOINT")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()
# print(result)


respond = requests.get(url=SHEETY_ENDPOINT)
data = respond.json()
# print(data)

SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

today_day = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

for exercise in result["exercises"]:
    # print(exercise)
    sheet_inputs = {
        "workout": {
            "date": today_day,
            "time": now_time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    respond = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs)
    # print(respond.text)
