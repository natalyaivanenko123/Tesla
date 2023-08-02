import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.page_shop import ShopPage
import pytest, allure


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Shop")
@allure.title("Test shop")
def test_login(driver):
    page = ShopPage(driver)
    page.open()
    page.find_header()
    page.find_product()
    page.find_purchasable()
    page.go_to_cart()
    page.find_checkout()
