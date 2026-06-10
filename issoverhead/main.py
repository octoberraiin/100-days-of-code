import requests
from datetime import datetime, timedelta
import smtplib
import time
import os

MY_LAT = os.environ.get("MY_LAT")
MY_LONG = os.environ.get("MY_LONG")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise_utc = datetime.fromisoformat(data["results"]["sunrise"].replace("Z", "+00:00"))
    sunset_utc = datetime.fromisoformat(data["results"]["sunset"].replace("Z", "+00:00"))
    sunrise_ist = sunrise_utc + timedelta(hours=5, minutes=30)
    sunset_ist = sunset_utc + timedelta(hours=5, minutes=30)

    sunrise = sunrise_ist.hour
    sunset = sunset_ist.hour

    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look Up!\n\nThe ISS is above you in the sky.")



