import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 63.232400,
    "lon": 26.755600,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It is raining! Get an umbrella!",
        to="whatsapp:+917899216256"
    )

    print(message.status)
    print(message.sid)




