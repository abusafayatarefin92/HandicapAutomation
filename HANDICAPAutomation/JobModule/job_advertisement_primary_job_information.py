from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class JobAdvertisementPrimaryJobInfo:
    def __init__(self,
                 edge_driver_handicap):
        self.edge_driver_handicap = edge_driver_handicap
        self.add_new_button = (By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/a')
        self.job_request_id_select = (By.XPATH, '//*[@id="recruitment_id"]')
        self.job_category_select = (By.XPATH, '//*[@id="category_id"]')
        self.job_type_select = (By.XPATH, '//*[@id="employment_status"]')
        self.role_type_select = (By.XPATH, '//*[@id="employee_type"]')
        self.publish_date_field = (By.XPATH, '//*[@id="published_date"]')
        self.publish_date_select = (By.XPATH, '/html/body/div[3]/div[1]/table/tbody/tr[4]/td[5]')
        self.application_deadline_field = (By.XPATH, '//*[@id="application_deadline"]')
        self.application_deadline_select = (By.XPATH, '/html/body/div[3]/div[1]/table/tbody/tr[5]/td[7]')
        self.special_instruction_text = (By.XPATH, '//*[@id="tinymce"]/p') #//*[@id="tinymce"]/p /html[1]/body[1]/p[1] (//p)[1] /html
        self.save_and_continue_button = (By.XPATH, '(//button[normalize-space()=\'Save and Continue\'])[1]')

    def open_job_advertisement_page(self,
                                    url):
        self.edge_driver_handicap.get(url)

    def click_add_new_button(self):
        self.edge_driver_handicap.find_element(*self.add_new_button).click()

    def select_all_drop_down_primary_job_info(self,
                                              job_request_id,
                                              job_category,
                                              job_type,
                                              role_type):
        job_request_id_value = self.edge_driver_handicap.find_element(*self.job_request_id_select)
        job_request_id_name = Select(job_request_id_value)
        job_request_id_name.select_by_visible_text(job_request_id)
        time.sleep(2)
        job_category_value = self.edge_driver_handicap.find_element(*self.job_category_select)
        job_category_name = Select(job_category_value)
        job_category_name.select_by_visible_text(job_category)
        time.sleep(2)
        job_type_value = self.edge_driver_handicap.find_element(*self.job_type_select)
        job_type_name = Select(job_type_value)
        job_type_name.select_by_visible_text(job_type)
        time.sleep(2)
        role_type_value = self.edge_driver_handicap.find_element(*self.role_type_select)
        role_type_name = Select(role_type_value)
        role_type_name.select_by_visible_text(role_type)

    def select_dates(self):
        self.edge_driver_handicap.find_element(*self.publish_date_field).click()
        time.sleep(2)
        self.edge_driver_handicap.find_element(*self.publish_date_select).click()
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.application_deadline_field).click()
        time.sleep(2)
        self.edge_driver_handicap.find_element(*self.application_deadline_select).click()

    def insert_all_text_value_primary_job_info(self,
                                               special_instruction):
        self.edge_driver_handicap.switch_to.frame('special_instruction_ifr')
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.special_instruction_text).send_keys(special_instruction)
        time.sleep(1)
        self.edge_driver_handicap.switch_to.default_content()

    def click_save_and_continue(self):
        self.edge_driver_handicap.find_element(*self.save_and_continue_button).click()
