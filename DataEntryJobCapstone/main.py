from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import requests
import re


FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSd9UDiax5DiGslsV3Ya4LKvj9Y2wvbH2SRlqSj5oSCgWX7Mjg/viewform?usp=publish-editor"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

# Web scraping
response = requests.get(ZILLOW_URL)
soup = BeautifulSoup(response.text, 'html.parser')

property_addresses = [address.getText().strip().replace(" |", ",") for address in soup.find_all(name="address")]
property_prices_messy = [price.getText() for price in soup.find_all(name="span", attrs={"data-test": "property-card-price"})]
property_prices = [re.match(r"\$[\d,]+", price).group() for price in property_prices_messy]
property_links = [link["href"] for link in soup.find_all(name="a", class_="property-card-link")]

number_of_properties = len(property_addresses)
print(f"Total Property Count: {number_of_properties}")

# Form action
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

for count in range(number_of_properties):
    driver.get(FORM_URL)
    sleep(2)
    address_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_entry.send_keys(property_addresses[count])
    price_entry.send_keys(property_prices[count])
    link_entry.send_keys(property_links[count])

    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    print(f"Forms Submitted Count: {count+1}")
