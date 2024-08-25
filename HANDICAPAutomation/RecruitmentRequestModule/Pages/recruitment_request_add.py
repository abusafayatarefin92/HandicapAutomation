from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class RecruitmentRequestAdd:
    def __init__(self,
                 edge_driver_handicap):
        self.edge_driver_handicap = edge_driver_handicap
        self.recruitment_request_click = (By.XPATH, '//*[@id="main-menu"]/ul/li[2]/a')
        self.hiring_manager_click = (By.XPATH, '//*[@id="main-menu"]/ul/li[2]/ul/li[2]/a')
        self.recruitment_request_add_button = (By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/a')
        self.project_or_department_select = (By.XPATH, '//*[@id="department"]')
        self.hiring_manager_text = (By.XPATH, '//*[@id="name_of_department"]')
        self.vacant_position_title_text = (By.XPATH, '//*[@id="position_title"]')
        self.job_description_select = (By.XPATH, '//*[@id="job_description"]')
        self.number_of_position_text = (By.XPATH, '//*[@id="number_of_position"]')
        self.employee_at_present_select = (By.XPATH, '//*[@id="employee_at_present"]')
        self.location_text = (By.XPATH, '//*[@id="location"]')
        self.type_of_appointment_select = (By.XPATH, '//*[@id="appointment_type"]')
        self.range_of_slary_from_text = (By.XPATH, '//*[@id="salary_range_from"]')
        self.type_of_recruitment_select = (By.XPATH, '//*[@id="recruitment_type"]')
        self.hod_assign_to_select = (By.XPATH, '//*[@id="hodam_id"]')
        self.range_of_slary_to_text = (By.XPATH, '//*[@id="salary_range_to"]')
        self.comments_text = (By.XPATH, '//*[@id="comments"]')
        self.submit_button = (By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[3]/div/div/div/div[2]/form/div[3]/button[2]')
        self.vacancy_caused_text = (By.XPATH, '//*[@id="vacancy_caused_due_to"]')
        self.job_starting_date = (By.XPATH, '//*[@id="job_starting_date"]')
        self.date_select = (By.XPATH, '/html/body/div[2]/div[1]/table/tbody/tr[5]/td[7]')

    def open_recruitment_request_add_page(self):
        self.edge_driver_handicap.find_element(*self.recruitment_request_click).click()
        time.sleep(2)
        self.edge_driver_handicap.find_element(*self.hiring_manager_click).click()

    def click_add_new_button(self):
        self.edge_driver_handicap.find_element(*self.recruitment_request_add_button).click()

    def select_date(self):
        self.edge_driver_handicap.find_element(*self.job_starting_date).click()
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.date_select).click()

    def select_all_type_of_dropdown_value(self,
                                          type_of_recruitment,
                                          hod_assign_to,
                                          project_or_department,
                                          job_description,
                                          employee_at_present,
                                          type_of_appointment):
        type_of_recruitment_value = self.edge_driver_handicap.find_element(*self.type_of_recruitment_select)
        type_of_recruitment_name = Select(type_of_recruitment_value)
        type_of_recruitment_name.select_by_visible_text(type_of_recruitment)
        time.sleep(2)
        hod_assign_to_value = self.edge_driver_handicap.find_element(*self.hod_assign_to_select)
        hod_assign_to_name = Select(hod_assign_to_value)
        hod_assign_to_name.select_by_visible_text(hod_assign_to)
        time.sleep(2)
        project_or_department_value = self.edge_driver_handicap.find_element(*self.project_or_department_select)
        project_or_department_name = Select(project_or_department_value)
        project_or_department_name.select_by_visible_text(project_or_department)
        time.sleep(2)
        job_description_value = self.edge_driver_handicap.find_element(*self.job_description_select)
        job_description_name = Select(job_description_value)
        job_description_name.select_by_visible_text(job_description)
        time.sleep(2)
        employee_at_present_value = self.edge_driver_handicap.find_element(*self.employee_at_present_select)
        employee_at_present_name = Select(employee_at_present_value)
        employee_at_present_name.select_by_visible_text(employee_at_present)
        time.sleep(2)
        type_of_appointment_value = self.edge_driver_handicap.find_element(*self.type_of_appointment_select)
        type_of_appointment_name = Select(type_of_appointment_value)
        type_of_appointment_name.select_by_visible_text(type_of_appointment)

    def insert_all_text_data(self,
                             hiring_manager,
                             vacant_position_title,
                             number_of_position,
                             location,
                             range_of_slary_from,
                             range_of_slary_to,
                             comments,
                             vacancy_caused):
        self.edge_driver_handicap.find_element(*self.hiring_manager_text).send_keys(hiring_manager)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.vacant_position_title_text).send_keys(vacant_position_title)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.number_of_position_text).send_keys(number_of_position)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.location_text).send_keys(location)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.range_of_slary_from_text).send_keys(range_of_slary_from)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.range_of_slary_to_text).send_keys(range_of_slary_to)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.comments_text).send_keys(comments)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.vacancy_caused_text).send_keys(vacancy_caused)

    def click_submit(self):
        self.edge_driver_handicap.find_element(*self.submit_button).click()
