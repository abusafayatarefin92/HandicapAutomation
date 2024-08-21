from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class HODApproval:
    def __init__(self, edge_driver_main):
        self.edge_driver_hod = edge_driver_main
        self.form_edit_button = (By.XPATH, '//*[@id="12"]/td[7]/a/i') #change the 'id' sequencially before every run
        self.country_hr_manager_select = (By.XPATH, '//*[@id="chrm_id"]')
        self.country_finance_manager_select = (By.XPATH, '//*[@id="cfm_id"]')
        self.i_agree_checkbox = (By.XPATH, '//*[@id="hodam_status"]')
        self.submit_button = (By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[3]/div/div/div/div[2]/form/div[3]/div[2]/button')
        self.comments_text = (By.XPATH, '//*[@id="hodam_comment"]')


    def open_hod_page(self, url):
        self.edge_driver_hod.get(url)

    def click_form_edit_button(self):
        self.edge_driver_hod.find_element(*self.form_edit_button).click()

    def select_all_dropdown(self, country_hr_manager, country_finance_manager):
        country_hr_manager_value = self.edge_driver_hod.find_element(*self.country_hr_manager_select)
        country_hr_manager_name = Select(country_hr_manager_value)
        country_hr_manager_name.select_by_visible_text(country_hr_manager)
        time.sleep(2)
        country_finance_manager_value = self.edge_driver_hod.find_element(*self.country_finance_manager_select)
        country_finance_manager_name = Select(country_finance_manager_value)
        country_finance_manager_name.select_by_visible_text(country_finance_manager)

    def insert_comments(self, comments):
        self.edge_driver_hod.find_element(*self.comments_text).send_keys(comments)

    def check_i_agree(self):
        self.edge_driver_hod.find_element(*self.i_agree_checkbox).click()

    def click_submit_button(self):
        self.edge_driver_hod.find_element(*self.submit_button).click()
