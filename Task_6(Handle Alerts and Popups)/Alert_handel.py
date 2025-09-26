from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(3)

wait=WebDriverWait(driver,10)

#alert_1
driver.find_element(By.ID,"alertButton").click()
alert=driver.switch_to.alert
print("Alert Text:",alert.text)
alert.accept()
time.sleep(3)

#alert_2
w = wait.until(EC.visibility_of_element_located((By.ID, "timerAlertButton")))
driver.execute_script("arguments[0].scrollIntoView(true);", w)
w.click()
time.sleep(6)
alert=driver.switch_to.alert
print("Alert Msg:",alert.text)
alert.accept()
time.sleep(3)

#alert_3
driver.find_element(By.ID,"confirmButton").click()
alert=driver.switch_to.alert
print("Alert Text:",alert.text)
alert.accept()
time.sleep(2)

result = driver.find_element(By.ID, "confirmResult").text
print("Result message:", result)

time.sleep(2)

#alert_4
driver.find_element(By.ID,"promtButton").click()
alert=driver.switch_to.alert
print("Alert Text:",alert.text)
alert.send_keys("Vimalraj")
alert.accept()
time.sleep(2)

result = driver.find_element(By.ID, "promptResult").text
print("Result message:", result)

ss=os.path.join(os.getcwd(),"verified.png")
driver.save_screenshot(ss)
driver.quit()