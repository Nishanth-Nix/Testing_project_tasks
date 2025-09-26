from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()
driver.get("https://automationexercise.com")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

time.sleep(2)

#  for Search Bar
driver.find_element(By.PARTIAL_LINK_TEXT, "Product").click()
driver.find_element(By.ID, "search_product").send_keys("Tshirt")
driver.find_element(By.ID, "submit_search").click()
time.sleep(3)

# for Category
women = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#Women']")))
driver.execute_script("arguments[0].scrollIntoView(true);", women)
women.click()
time.sleep(3)

# for Click "Dress"
element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Dress')]")))
driver.execute_script("arguments[0].click();", element)
time.sleep(3)

msg = driver.find_elements(By.TAG_NAME, "h2")
print("Actual h2 text:", msg[2].text)

if "women - dress products" in msg[2].text.lower():
    print("Category is verified:", msg[2].text)
else:
    print("Failed")
#for screen shot
ss=os.path.join(os.getcwd(),"verified.png")
driver.save_screenshot(ss)

time.sleep(3)
driver.quit()
