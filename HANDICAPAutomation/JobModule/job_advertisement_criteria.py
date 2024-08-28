from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class JobAdvertisementCriteria:
    def __init__(self,
                 edge_driver_handicap):
        self.edge_driver_handicap = edge_driver_handicap
        self.add_button = (By.XPATH, '(//a[@class=\'btn btn-danger btn-sm1\'])[7]')
        self.criteria_text = (By.XPATH, '(//textarea[@id=\'criteria\'])[1]')
        self.point_text = (By.XPATH, '(//input[@name=\'point[]\'])[1]')
        self.status_select = (By.XPATH, '(//select[@name=\'status[]\'])[1]')
        self.add_row_button = (By.XPATH, '//*[@id="add-row-btn"]')
        self.criteria_text2 = (By.XPATH, '(//textarea[@id=\'criteria\'])[2]')
        self.point_text2 = (By.XPATH, '(//input[@name=\'point[]\'])[2]')
        self.status_select2 = (By.XPATH, '(//select[@name=\'status[]\'])[2]')
        self.save_button = (By.XPATH, '(//button[normalize-space()=\'Save\'])[1]')


    def click_add_button(self):
        self.edge_driver_handicap.find_element(*self.add_button).click()

    def insert_all_text_fields(self, criteria, point):
        self.edge_driver_handicap.find_element(*self.criteria_text).send_keys(criteria)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.point_text).send_keys(point)

    def select_status(self, status):
        status_value = self.edge_driver_handicap.find_element(*self.status_select)
        status_name = Select(status_value)
        status_name.select_by_visible_text(status)

    def click_add_row_button(self):
        self.edge_driver_handicap.find_element(*self.add_row_button).click()

    def insert_all_text_fields2(self, criteria, point):
        self.edge_driver_handicap.find_element(*self.criteria_text2).send_keys(criteria)
        time.sleep(1)
        self.edge_driver_handicap.find_element(*self.point_text2).send_keys(point)

    def select_status2(self, status):
        status_value = self.edge_driver_handicap.find_element(*self.status_select2)
        status_name = Select(status_value)
        status_name.select_by_visible_text(status)

    def click_save_button(self):
        self.edge_driver_handicap.find_element(*self.save_button).click()
