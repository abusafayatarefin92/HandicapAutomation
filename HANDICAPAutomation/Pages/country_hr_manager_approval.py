from selenium.webdriver.common.by import By
import time

class CountryHRManagerApproval:
    def __init__(self, edge_driver_main):
        self.edge_driver_country = edge_driver_main
        self.country_hr_manager_approval_edit = (By.XPATH, '//*[@id="12"]/td[7]/a/i') #change the 'id' sequencially before every run
        self.i_agree_checkbox = (By.XPATH, '//*[@id="chrm_status"]')
        self.submit_button = (By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[3]/div/div/div/div[2]/form/div[3]/div[2]/button')

    def open_country_manager_page(self, url):
        self.edge_driver_country.get(url)

    def click_country_hr_manager_approval_edit_and_i_agree_checkbox(self):
        self.edge_driver_country.find_element(*self.country_hr_manager_approval_edit).click()
        time.sleep(2)
        self.edge_driver_country.find_element(*self.i_agree_checkbox).click()

    def click_submit_button(self):
        self.edge_driver_country.find_element(*self.submit_button).click()