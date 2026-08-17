from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/1SZ4Mi1hyx2CvGap6G5bpGsTet1dJ24P"
FACEBARK_EMAIL = "anything@gmail.com"
FACEBARK_PASSWORD = "anything"

driver = webdriver.Chrome()
driver.get(TINDOG_URL)

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(1)
facebark_button = driver.find_element(By.CLASS_NAME, value='btn-facebark')
facebark_button.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.ID, value='email')
password = driver.find_element(By.ID, value='pass')
email.send_keys(FACEBARK_EMAIL)
password.send_keys(FACEBARK_PASSWORD)
password.send_keys(Keys.ENTER)

sleep(1)
driver.switch_to.window(base_window)
print(driver.title)

sleep(2)
driver.find_element(By.XPATH, value='//button[text()="Allow"]').click()
sleep(1)
driver.find_element(By.XPATH, value='//button[text()="Not interested"]').click()
sleep(1)
driver.find_element(By.XPATH, value='//button[text()="I Accept"]').click()

for n in range(20):
    sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        sleep(2)

driver.quit()
