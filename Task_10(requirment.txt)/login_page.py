from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open_login_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()
