from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hw_6.pages.locators import header_locators
import allure
import pytest

def test_header(driver):
    wait.until(EC.presence_of_element_located(header_locators.header))

    buttons = driver.find_elements(header_locators.header_btn)
    for item in buttons:
        ActionChains(driver).move_to_element(item).perform()
        assert(item.is_displayed())

    # Нахождение элементов на странице
    logo = driver.find_element(header_locators.header_logo)
    ActionChains(driver).move_to_element(logo).perform()
    assert(logo.is_displayed())

@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Авторизация")
@allure.title("Авторизация с валидными данными")
def test_login(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()
    home_page.go_to_login_screen()
    home_page.can_see_login_form()
    home_page.fill_login_inputs_valid_data_and_submit()
    profile_page = ProfilePage(driver)
    assert profile_page.check_for_my_orders_tab_on_page(), "Вы не авторизовались"
