from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
wait = WebDriverWait(driver, 10)

with open(r"C:\Users\nishanth\OneDrive\Desktop\Tasks\Task_2\data.csv", 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)

    for input in reader:
        firstname = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        firstname.clear()
        firstname.send_keys(input['firstname'])

        secname = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
        secname.clear()
        secname.send_keys(input['lastname'])

        email = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
        email.clear()
        email.send_keys(input['email'])

        number = driver.find_element(By.XPATH, "(//input[@type='text'])[4]")
        number.clear()
        number.send_keys(input['number'])

        time.sleep(3)

        pass_input = wait.until(EC.visibility_of_element_located((By.ID, "uploadPicture")))
        driver.execute_script("arguments[0].scrollIntoView(true);", pass_input)
        ActionChains(driver).move_to_element(pass_input).perform()
        pass_input.clear()
        pass_input.send_keys(input['picture'])

        time.sleep(3)
        print("upload of picture is completed")

driver.quit()
