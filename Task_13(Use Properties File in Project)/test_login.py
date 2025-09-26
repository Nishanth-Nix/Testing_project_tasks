import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

config = configparser.RawConfigParser()
config.read('test.properties')

url = config.get('DEFAULT', 'url')
username = config.get('DEFAULT', 'username')
password = config.get('DEFAULT', 'password')
username_id = config.get('DEFAULT', 'username_id')
password_id = config.get('DEFAULT', 'password_id')
login_button_id = config.get('DEFAULT', 'login_button_id')

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

driver.find_element(By.ID, username_id).send_keys(username)
driver.find_element(By.ID, password_id).send_keys(password)
driver.find_element(By.ID, login_button_id).click()

time.sleep(2)

if "inventory" in driver.current_url:
    print("Login successful")
else:
    print("Login failed")

driver.quit()
