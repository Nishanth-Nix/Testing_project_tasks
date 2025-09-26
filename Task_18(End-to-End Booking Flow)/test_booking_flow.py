import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://phptravels.net/login")
    yield driver
    time.sleep(3)
    driver.quit()


def take_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(f"screenshots/{name}.png")


def test_login(driver):
    wait = WebDriverWait(driver, 20)

    driver.find_element(By.NAME, "email").send_keys("user@phptravels.com")
    driver.find_element(By.NAME, "password").send_keys("demouser")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

    # Wait for the dashboard
    welcome_text = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Hi')]"))
    ).text

    assert "Hi" in welcome_text
    take_screenshot(driver, "01_login")


def test_search_hotel(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://phptravels.net/hotels")

    # Click search field
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(),'Search by Hotel or City Name')]"))
    ).click()

    # Type "Dubai" and select from dropdown
    city_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))
    city_input.send_keys("Dubai")
    time.sleep(2)  # Allow dropdown to load
    city_input.send_keys(Keys.ENTER)

    # Click Search
    driver.find_element(By.ID, "submit").click()

    # Wait for hotel results
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "card")))
    assert "hotels" in driver.current_url
    take_screenshot(driver, "02_search_hotel")


def test_select_hotel(driver):
    wait = WebDriverWait(driver, 20)

    # Click the first hotel card
    hotel_card = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "card")))
    hotel_card.click()

    # Wait for hotel details page
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "book_button")))
    assert "details" in driver.current_url
    take_screenshot(driver, "03_select_hotel")


def test_book_hotel(driver):
    wait = WebDriverWait(driver, 20)

    # Wait and click "Book Now" button
    book_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "book_button")))
    book_btn.click()

    # Wait for booking/checkout page
    wait.until(EC.presence_of_element_located((By.ID, "bookingdetails")))
    assert "checkout" in driver.current_url
    take_screenshot(driver, "04_book_hotel")
