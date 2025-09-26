from selenium import webdriver
from login_page import LoginPage
import time

def test_login():
    driver = webdriver.Chrome()
    login = LoginPage(driver)

    login.open_login_page()
    login.login("Admin", "admin123")

    time.sleep(3)  # Wait for page to load
    assert "dashboard" in driver.current_url.lower()

    print("Login successful!")
    driver.quit()

if __name__ == "__main__":
    test_login()
