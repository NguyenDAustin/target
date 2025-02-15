"""
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium"
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

import time

chrome_options = Options()
chrome_options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.target.com/p/pokemon-trading-card-game-scarlet-38-violet-surging-sparks-booster-bundle/-/A-91619929#lnk=sametab")

while True:
    try:
        input_element = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-test="shippingButton"]'))
        )
        input_element.click()
        break

    except TimeoutException:
        print("refresh")
        driver.refresh()
        WebDriverWait(driver, 3).until(lambda d: d.execute_script('return document.readyState') == 'complete')

# To go to cart from the add button
""" 
input_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "View cart")]'))
)
input_element.click()
"""

driver.get("https://www.target.com/cart")

input_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Check out")]'))
)
input_element.click()

WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

input_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@data-test="placeOrderButton"]'))
)
input_element.click()

# Pin
input_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'enter-pin'))
)

driver.execute_script("arguments[0].focus();", input_element)
input_element.send_keys("1234")

input_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@data-test="confirm-button"]'))
)
input_element.click()

# Card number
input_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'credit-card-number-input'))
)

driver.execute_script("arguments[0].focus();", input_element)
input_element.send_keys("1234 5678 9101 1121")

input_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@data-test="verify-card-button"]'))
)
input_element.click()
