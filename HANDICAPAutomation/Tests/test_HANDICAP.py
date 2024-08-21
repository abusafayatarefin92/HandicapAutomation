import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from Pages.login_page import LoginPage
from Pages.recruitment_request_add import RecruitmentRequestAdd
from Pages.HOD_approval import HODApproval
from Pages.country_hr_manager_approval import CountryHRManagerApproval
from Pages.country_finance_manager_approval import CountryFinanceManagerApproval

@pytest.fixture()
def edge_driver_func():
    edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    edge_driver.maximize_window()
    edge_driver.implicitly_wait(10)

    yield edge_driver

    edge_driver.close()
    edge_driver.quit()


def test_handicap(edge_driver_func):
    #login
    login_page = LoginPage(edge_driver_func)
    login_page.open_page_and_give_credentials('https://test.jobs.hi-bd.org/admin/login',
                                              'arefin_super_admin',
                                              '123456')
    time.sleep(3)
    login_page.click_login_button()
    time.sleep(3)

    #Add new recruitment Request
    recruitment_request_add = RecruitmentRequestAdd(edge_driver_func)
    recruitment_request_add.open_recruitment_request_add_page()
    time.sleep(1)
    recruitment_request_add.select_date()
    time.sleep(1)
    recruitment_request_add.select_all_type_of_dropdown_value('External Recruitment',
                                                              'Arefin Super Admin ( Super Admin ) - Super Admin',
                                                              'Finance',
                                                              'Project Officer_Job Description',
                                                              'No',
                                                              'Permanent')
    time.sleep(1)
    recruitment_request_add.insert_all_text_data('Meftaul Haque',
                                                 'Executive',
                                                 '2',
                                                 'Dhaka',
                                                 '15000',
                                                 '20000',
                                                 'Aliquam et luctus libero. Nulla facilisi.',
                                                 'Aliquam et luctus libero. Nulla facilisi.')
    time.sleep(1)
    recruitment_request_add.click_submit()
    print('\nSuccessfully added a recruitment request\n')
    time.sleep(4)

    job_id = edge_driver_func.find_element(By.XPATH,
                                           '//*[@id="12"]/td[2]/a').text #change the 'id' sequencially before every run

    #HOD approval
    hod_approval = HODApproval(edge_driver_func)
    hod_approval.open_hod_page('https://test.jobs.hi-bd.org/admin/hodam-recruitment-request')
    time.sleep(2)

    recruitment_id_hod = edge_driver_func.find_element(By.XPATH,
                                                       '//*[@id="12"]/td[2]/a').text #change the 'id' sequencially before every run

    if recruitment_id_hod == job_id:
        hod_approval.click_form_edit_button()
        time.sleep(3)
        hod_approval.select_all_dropdown('Arefin Super Admin ( Super Admin ) - Super Admin',
                                         'Arefin Super Admin ( Super Admin ) - Super Admin')
        time.sleep(1)
        hod_approval.insert_comments('Aliquam et luctus libero. Nulla facilisi.')
        time.sleep(1)
        hod_approval.check_i_agree()
        time.sleep(1)
        hod_approval.click_submit_button()
        time.sleep(3)
        print('Successfully approved by HOD\n')

        # Country HR Manager Approval
        country_hr_manager_approval = CountryHRManagerApproval(edge_driver_func)
        country_hr_manager_approval.open_country_manager_page(
            'https://test.jobs.hi-bd.org/admin/chrm-recruitment-request')
        time.sleep(2)

        recruitment_id_country_hr_manager = edge_driver_func.find_element(By.XPATH,
                                                                          '//*[@id="12"]/td[2]/a').text #change the 'id' sequencially before every run

        if recruitment_id_country_hr_manager == job_id:
            country_hr_manager_approval.click_country_hr_manager_approval_edit_and_i_agree_checkbox()
            time.sleep(2)
            country_hr_manager_approval.click_submit_button()
            time.sleep(3)
            print('Successfully approved by Country HR Manager\n')
        else:
            print('Recruitment ID doesn\'t match in Country HR Manager Approval')

        # Country Finance Manager Approval
        country_finance_manager_approval = CountryFinanceManagerApproval(edge_driver_func)
        country_finance_manager_approval.open_country_manager_page(
            'https://test.jobs.hi-bd.org/admin/cfm-recruitment-request')
        time.sleep(2)

        recruitment_id_country_finance_manager = edge_driver_func.find_element(By.XPATH,
                                                                               '//*[@id="12"]/td[2]/a').text #change the 'id' sequencially before every run

        if recruitment_id_country_finance_manager == job_id:
            country_finance_manager_approval.click_country_finance_manager_approval_edit_and_i_agree_checkbox()
            time.sleep(2)
            country_finance_manager_approval.click_submit_button()
            time.sleep(3)
            print('Successfully approved by Country Finance Manager\n')
        else:
            print('Recruitment ID doesn\'t match in Country Finance Manager Approval')
    else:
        print('Recruitment ID doesn\'t match in HOD approval')
