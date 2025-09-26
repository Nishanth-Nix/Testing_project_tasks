import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager

# Manually driver path
EDGE_DRIVER_PATH = r"C:\Users\VIMAL RAJ\Downloads\edgedriver_win64\msedgedriver.exe"

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_login(browser):
    driver = None
    try:
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "edge":
            service = EdgeService(executable_path=EDGE_DRIVER_PATH)
            driver = webdriver.Edge(service=service)
        else:
            pytest.skip("Unsupported browser")

        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        assert "You logged into a secure area!" in driver.page_source

    finally:
        if driver:
            driver.quit()
