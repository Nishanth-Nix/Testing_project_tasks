import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/upload/")
driver.maximize_window()

time.sleep(2)

os.system(r'"C:\Users\VIMAL RAJ\OneDrive\Desktop\Tasks\Task_8(File Upload with AutoIT)\upload_script.exe"')
time.sleep(2)


driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "submitbutton").click()

time.sleep(3)
driver.quit()
