from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from Data.fixed_data import FixedData

fixed_data = FixedData()
job_advertisement_edit = fixed_data.job_advertisement_edit_button_xpath

class JobAdvertisementMoreJobInfo:
    def __init__(self,
                 edge_driver_handicap):
        self.edge_driver_handicap = edge_driver_handicap
        self.edit_button = (By.XPATH, job_advertisement_edit)
        self.job_level_select = (By.XPATH, '//*[@id="job_level"]')
        self.workplace_select = (By.XPATH, '//*[@id="workplace"]')
        self.area_or_headquarters_select = (By.XPATH, '//*[@id="area_headquarters"]')
        self.job_context_text = (By.XPATH, '//*[@id="tinymce"]')
        self.job_responsibility_text = (By.XPATH, '//*[@id="tinymce"]')
        self.job_location_text = (By.XPATH, '//*[@id="job_location"]')
        self.additional_salary_text = (By.XPATH, '//*[@id="tinymce"]')
        self.other_benefits_text = (By.XPATH, '//*[@id="tinymce"]')
        self.show_salary_click = (By.XPATH, '//*[@id="show_salary"]')
        self.festival_bonus_click = (By.XPATH, '//*[@id="inlineCheckbox-9"]')
        self.leave_click = (By.XPATH, '//*[@id="inlineCheckbox-8"]')
        self.save_button = (By.XPATH, '(//button[contains(text(),\'Save\')])[1]')

    def open_job_advertisement_more_info_page(self,
                                              url):
        self.edge_driver_handicap.get(url)

    def click_edit_button(self):
        self.edge_driver_handicap.find_element(*self.edit_button).click()

    def select_all_dropdowns(self,
                             job_level,
                             workplace,
                             area_or_headquarters):
        job_level_value = self.edge_driver_handicap.find_element(*self.job_level_select)
        job_level_name = Select(job_level_value)
        job_level_name.select_by_visible_text(job_level)
        time.sleep(1)
        workplace_value = self.edge_driver_handicap.find_element(*self.workplace_select)
        workplace_name = Select(workplace_value)
        workplace_name.select_by_visible_text(workplace)
        time.sleep(1)
        area_or_headquarters_value = self.edge_driver_handicap.find_element(*self.area_or_headquarters_select)
        area_or_headquarters_name = Select(area_or_headquarters_value)
        area_or_headquarters_name.select_by_visible_text(area_or_headquarters)

    def insert_data_all_text_fields(self,
                                    job_context,
                                    job_responsibility,
                                    job_location,
                                    additional_salary,
                                    other_benefits):
        self.edge_driver_handicap.switch_to.frame('job_context_ifr')
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.job_context_text).send_keys(job_context)
        time.sleep(1)
        self.edge_driver_handicap.switch_to.default_content()
        time.sleep(1)
        self.edge_driver_handicap.switch_to.frame('job_responsibility_ifr')
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.job_responsibility_text).send_keys(job_responsibility)
        time.sleep(1)
        self.edge_driver_handicap.switch_to.default_content()
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.job_location_text).send_keys(job_location)
        time.sleep(1)
        self.edge_driver_handicap.switch_to.frame('additional_salary_ifr')
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.additional_salary_text).send_keys(additional_salary)
        time.sleep(1)
        self.edge_driver_handicap.switch_to.default_content()
        time.sleep(1)
        self.edge_driver_handicap.switch_to.frame('other_benefits_ifr')
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.other_benefits_text).send_keys(other_benefits)
        time.sleep(1)
        self.edge_driver_handicap.switch_to.default_content()

    def click_option_and_checkboxes(self):
        self.edge_driver_handicap.find_element(*self.show_salary_click).click()
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.festival_bonus_click).click()
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.leave_click).click()

    def click_save(self):
        self.edge_driver_handicap.find_element(*self.save_button).click()
