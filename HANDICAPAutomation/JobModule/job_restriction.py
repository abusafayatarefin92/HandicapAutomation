from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class JobRestriction:
    def __init__(self,
                 edge_driver_handicap):
        self.edge_driver_handicap = edge_driver_handicap
        self.add_new_button = (By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/a')
        self.job_request_id_select = (By.XPATH, '//*[@id="recruitment_id"]')
        self.question1_text = (By.XPATH, '//*[@id="question1"]')
        self.question2_text = (By.XPATH, '//*[@id="question2"]')
        self.question3_text = (By.XPATH, '//*[@id="question3"]')
        self.question4_text = (By.XPATH, '//*[@id="question4"]')
        self.question5_text = (By.XPATH, '//*[@id="question5"]')
        self.question6_text = (By.XPATH, '//*[@id="question6"]')
        self.question7_text = (By.XPATH, '//*[@id="question7"]')
        self.question8_text = (By.XPATH, '//*[@id="question8"]')
        self.question9_text = (By.XPATH, '//*[@id="question9"]')
        self.question10_text = (By.XPATH, '//*[@id="question10"]')
        self.save_button = (By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[3]/div/div/div/div[2]/form/div[2]/div[21]/button[1]')

    def open_job_restriction_page(self, url):
        self.edge_driver_handicap.get(url)

    def click_add_new_button(self):
        self.edge_driver_handicap.find_element(*self.add_new_button).click()

    def select_job_request_id(self, job_request_id):
        job_request_id_value = self.edge_driver_handicap.find_element(*self.job_request_id_select)
        job_request_id_name = Select(job_request_id_value)
        job_request_id_name.select_by_visible_text(job_request_id)

    def insert_all_text_fields(self,
                               question1,
                               question2,
                               question3,
                               question4,
                               question5,
                               question6,
                               question7,
                               question8,
                               question9,
                               question10):
        self.edge_driver_handicap.find_element(*self.question1_text).send_keys(question1)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.question2_text).send_keys(question2)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.question3_text).send_keys(question3)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.question4_text).send_keys(question4)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.question5_text).send_keys(question5)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.question6_text).send_keys(question6)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.question7_text).send_keys(question7)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.question8_text).send_keys(question8)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.question9_text).send_keys(question9)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.question10_text).send_keys(question10)

    def click_save_button(self):
        self.edge_driver_handicap.find_element(*self.save_button).click()
