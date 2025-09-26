from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Passw23")

submit = wait.until(EC.visibility_of_element_located((By.ID, "submit")))
driver.execute_script("arguments[0].scrollIntoView(true);", submit)
submit.click()

screenshot_path = os.path.join(os.getcwd(), "login_failure.png")
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved at: {screenshot_path}")

driver.quit()