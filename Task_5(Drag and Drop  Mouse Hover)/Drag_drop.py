from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")

iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(iframe)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

time.sleep(2)
dropped_text = target.text
print("Text after drop:", dropped_text)

bg_color = target.value_of_css_property("background-color")
print("Background color after drop:", bg_color)
if "Dropped!" in dropped_text:
    print("Drag and drop text: Passed")
else:
    print("Drag and drop text: Failed")

if "rgba(255, 250, 144, 1" in bg_color:
    print("Background color change: Passed")
else:
    print("Background color change: Failed")

ss=os.path.join(os.getcwd(),"Passed.png")
driver.save_screenshot(ss)
driver.quit()
