from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class JobAdvertisementCandidateRequirements:
    def __init__(self,
                 edge_driver_handicap):
        self.edge_driver_handicap = edge_driver_handicap
        self.candidate_requirements_tab = (By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[3]/div/div/div/div[2]/ul/li[3]/a')
        self.educational_qualification_text = (By.XPATH, '//*[@id="educational_qualification"]')
        self.training_or_trade_courses_text = (By.XPATH, '//*[@id="training_course"]')
        self.profesional_certification_text = (By.XPATH, '//*[@id="professional_certification"]')
        self.additional_requirements_text = (By.XPATH, '//*[@id="tinymce"]')
        self.minimum_age_text = (By.XPATH, '//*[@id="min_age"]')
        self.maximum_age_text = (By.XPATH, '//*[@id="max_age"]')
        self.area_of_expertise_select = (By.XPATH, '//*[@id="expertise"]')
        self.skills_select = (By.XPATH, '//*[@id="skills"]')
        self.no_experience_click = (By.XPATH, '//*[@id="is_experience_required1"]')
        self.freshers_encouragement_click = (By.XPATH, '//*[@id="is_fresher_apply"]')
        self.both_gender_select = (By.XPATH, '//*[@id="Both"]')
        self.save_button = (By.XPATH, '//*[@id="tabs-3"]/form/div[4]/button[1]')

    def click_candidate_requirements_tab(self):
        self.edge_driver_handicap.find_element(*self.candidate_requirements_tab).click()

    def insert_all_text_fields_data(self,
                                    educational_qualification,
                                    training_or_trade_courses,
                                    profesional_certification,
                                    additional_requirements,
                                    minimum_age,
                                    maximum_age):
        self.edge_driver_handicap.find_element(*self.educational_qualification_text).send_keys(educational_qualification)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.training_or_trade_courses_text).send_keys(training_or_trade_courses)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.profesional_certification_text).send_keys(profesional_certification)
        time.sleep(1)
        self.edge_driver_handicap.switch_to.frame('additional_requirements_ifr')
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.additional_requirements_text).send_keys(additional_requirements)
        time.sleep(1)
        self.edge_driver_handicap.switch_to.default_content()
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.minimum_age_text).send_keys(minimum_age)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.maximum_age_text).send_keys(maximum_age)

    def select_all_dropdown_fields(self,
                                   area_of_expertise,
                                   skills):
        area_of_expertise_value = self.edge_driver_handicap.find_element(*self.area_of_expertise_select)
        area_of_expertise_name = Select(area_of_expertise_value)
        area_of_expertise_name.select_by_visible_text(area_of_expertise)
        time.sleep(1)
        skills_value = self.edge_driver_handicap.find_element(*self.area_of_expertise_select)
        skills_name = Select(skills_value)
        skills_name.select_by_visible_text(skills)

    def click_all_options_checkboxes(self):
        self.edge_driver_handicap.find_element(*self.no_experience_click).click()
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.freshers_encouragement_click).click()
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.both_gender_select).click()

    def click_save_button(self):
        self.edge_driver_handicap(*self.save_button).click()