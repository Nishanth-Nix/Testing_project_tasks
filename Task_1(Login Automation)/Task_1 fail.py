from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
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
#ActionChains(driver).move_to_element(submit).perform()
submit.click()

time.sleep(2)
try:
    success_message = driver.find_element(By.TAG_NAME, "h1")
    if "Logged In Successfully" in success_message.text:
        print("Login success")
    else:
        print("Unexpected message:", success_message.text)

except:
    error_element = driver.find_element(By.ID, "error")
    if error_element.is_displayed():
        print("Login failed:", error_element.text)
    
        screenshot_path = os.path.join(os.getcwd(), "login_failure.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

driver.quit()
