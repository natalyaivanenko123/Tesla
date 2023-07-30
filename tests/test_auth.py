import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from natalya_ivanenko.hw_6.pages.locators import auth_locators
from natalya_ivanenko.hw_6.pages.page_auth import AuthPage
import pytest, allure


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Авторизация")
@allure.title("Авторизация с валидными данными")
def test_login(driver):
    home_page = AuthPage(driver)
    home_page.open()
    home_page.send_email()
    home_page.click_submit()
    home_page.send_pass()
    home_page.click_submit()
    home_page.check_dashboard()
