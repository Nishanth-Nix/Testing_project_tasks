import pytest
from selenium import webdriver
from configparser import ConfigParser
from page.login_page import LoginPage
from utilities.csv_reader import get_credentials
from utilities.logger import get_logger

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    config = ConfigParser()
    config.read("config/config.ini")
    driver.get(config["DEFAULT"]["base_url"])
    driver.maximize_window()
    yield driver
    driver.quit()

def test_end_to_end(setup):
    driver = setup
    logger = get_logger()
    username, password = get_credentials("data/credentials.csv")

    login = LoginPage(driver)
    login.login(username, password)
    logger.info("Login done")
    
    assert "cart" in driver.current_url.lower()
