from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://automationexercise.com/")
time.sleep(3)

driver.execute_script("window.scrollTo(0, 500);")
time.sleep(2)

women = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#Women']")))
driver.execute_script("arguments[0].scrollIntoView(true);", women)
women.click()
time.sleep(3)

element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Dress')]")))
driver.execute_script("arguments[0].click();", element)
time.sleep(3)

category_header = driver.find_element(By.XPATH, "//h2[@class='title text-center']").text
if  "WOMEN - DRESS PRODUCTS" in category_header.upper():
    print("Filter validation passed")


ss=os.path.join(os.getcwd(),"filtered_results.png")
driver.save_screenshot(ss)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

print("Page scrolled to bottom")

driver.quit()
