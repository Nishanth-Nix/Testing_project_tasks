from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('the user is on the login page')
def step_open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()

@when('the user enters valid credentials')
def step_enter_credentials(context):
    context.driver.find_element(By.NAME, "username").send_keys("Admin")
    context.driver.find_element(By.NAME, "password").send_keys("admin123")

@when('clicks the login button')
def step_click_login(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

@then('the user should be redirected to the dashboard')
def step_verify_dashboard(context):
    assert "dashboard" in context.driver.current_url.lower()
    context.driver.quit()
