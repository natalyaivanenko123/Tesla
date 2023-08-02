import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.page_demo import DemoPage
import pytest, allure


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Demo")
@allure.title("Test demo driver")
def test_login(driver):
    page = DemoPage(driver)
    page.open()
    page.find_and_check_models()
    page.fill_form()
    page.fill_form()
    page.find_label()
    page.check_errors()
    page.find_button_1()
    page.find_button_2()
    page.find_button_3()
    page.find_button_4()
    page.find_success_button()

