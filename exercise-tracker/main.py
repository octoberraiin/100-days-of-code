import requests
from datetime import datetime, date, timedelta
import os

AGE = int(os.environ["AGE"])
GENDER = os.environ["GENDER"]

EXERCISE_ENDPOINT = os.environ["EXERCISE_ENDPOINT"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]


exercise_text = input("Tell me which exercises you did ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_data = {
    "query": exercise_text,
    "age": AGE,
    "gender": GENDER,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_data, headers=headers)
result = response.json()
print(result)

# ---------------------------------------------------------------------------------- #


user_date = input("Tell me date of entry (today/yesterday/custom): ")
user_time = input("Tell me time of entry(now/custom): ")

if user_date == "today":
    date = datetime.now().strftime("%d/%m/%Y")
elif user_date == "yesterday":
    date = (date.today() - timedelta(days=1)).strftime("%d/%m/%Y")
else:
    date = user_date


if user_time == "now":
    time = datetime.now().strftime("%H:%M")
else:
    time = user_time


# ---------------------------------------------------------------------------------- #


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs)
    print(sheet_response.json())

