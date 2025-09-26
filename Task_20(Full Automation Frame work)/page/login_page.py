from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_link = (By.LINK_TEXT, "Log in")
        self.email = (By.ID, "Email")
        self.password = (By.ID, "Password")
        self.login_btn = (By.XPATH, "//button[text()='Log in']")

    def login(self, user, pwd):
        self.driver.find_element(*self.login_link).click()
        self.driver.find_element(*self.email).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()
