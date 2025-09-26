import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@allure.title("Open Google Homepage Test")
@allure.description("Test opening Google homepage using ChromeDriver.")
def test_open_google():
    service = Service(r"C:\Users\Administrator\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    with allure.step("Open Google homepage"):
        driver.get("https://www.google.com/")

    with allure.step("Print success message"):
        print("Successfully opened Google homepage")

    driver.quit()
