from selenium.webdriver.common.by import By
import time

class LoginPage:

    def __init__(self, edge_driver):
        self.edge_driver = edge_driver
        self.username_textbox = (By.XPATH, '//*[@id="username"]')
        self.password_textbox = (By.XPATH, '//*[@id="password"]')
        self.login_button = (By.XPATH,'//*[@id="signup"]/form/div[3]/button')

    def open_page_and_give_credentials(self,
                                       url,
                                       username,
                                       password):
        self.edge_driver.get(url)
        time.sleep(3)
        self.edge_driver.find_element(*self.username_textbox).send_keys(username)
        time.sleep(3)
        self.edge_driver.find_element(*self.password_textbox).send_keys(password)

    def click_login_button(self):
        self.edge_driver.find_element(*self.login_button).click()