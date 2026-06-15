import requests
import requests_cache
import os
from twilio.rest import Client

# ----------------------------- CONSTANTS -------------------------- #

requests_cache.install_cache("stock&news_cache")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

STOCK_PARAMS = {
    "apikey": STOCK_API_KEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
}

NEWS_PARAMS = {
    "apikey": NEWS_API_KEY,
    "q": COMPANY_NAME,
}

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")



# ------------------------------- PROGRAM --------------------------- #

response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
# diff_percent = round((difference / float(yesterday_closing_price)) * 100)
diff_percent = 8

if difference > 0:
    icon = "🔺"
else:
    icon = "🔻"

if abs(diff_percent) >= 5:
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {icon}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="+15187192692",
            body=article,
            to="+917899216256"
        )

        print(message.status)
        print(message.sid)
        print(message.subresource_uris)
