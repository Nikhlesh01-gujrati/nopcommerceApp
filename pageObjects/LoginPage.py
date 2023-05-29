from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element("id", "Email").clear()
        self.driver.find_element("id", "Email").send_keys(username)

    def setPassword(self, password):
        self.driver.find_element("id", "Password").clear()
        self.driver.find_element("id", "Password").send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath", "//button[@type='submit']").click()

    def clickLogout(self):
        self.driver.find_element("xpath", "//a[text()='Logout']").click()
