from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

EMAIL = os.environ["EMAIL_ADDRESS"]
PASSWORD = os.environ["EMAIL_PASSWORD"]

# Load environment variables from .env file
load_dotenv()

url = "https://appbrewery.github.io/instant_pot/"
header = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
price = soup.find(class_="a-offscreen").get_text()

price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

# ====================== Send an Email ===========================

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 100
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))