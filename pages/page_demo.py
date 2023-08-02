from selenium.common import NoSuchElementException
from natalya_ivanenko.hw_6.pages.base_page import BasePage
from natalya_ivanenko.hw_6.pages.locators import demo_locators
import allure
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на страницу"):
            self.driver.get("https://www.tesla.com/drive")
            wait = WebDriverWait(self.driver, 10)
            wait.until(demo_locators.models)

    def find_and_check_models(self):
        with allure.step("Find and check models"):
            models = self.find_elements(demo_locators.models)
            for item in models:
                ActionChains(self.driver).move_to_element(item).perform()
                assert (item.is_displayed())
                assert (item.is_enabled())
                models[0].click()
                assert (models[0])

    def fill_form(self):
        with allure.step("Fill form"):
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            input = self.find_element(demo_locators.edit_firstname)
            input.send_keys("Natalja")

            input = self.find_element(demo_locators.edit_lastname)
            input.send_keys("Ivanenko")

            input = self.find_element(demo_locators.edit_phonenumber)
            input.send_keys("2015550123")

            input = self.find_element(demo_locators.edit_usermail)
            input.send_keys("hello@mail.ru")

            input = self.find_element(demo_locators.edit_zipcode)
            input.send_keys("78585")
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)

    def find_label(self):
        with allure.step("Find label"):
            button = self.find_element(demo_locators.label)
            button.click()


    def check_errors(self):
        with allure.step("Check errors"):
            errors = self.driver.find_elements(demo_locators.text)
            for error in errors:
                assert (not error.is_displayed())


    def find_button_1(self):
        with allure.step("Find button 1"):
            submit = self.driver.find_element(demo_locators.ajax0)
            assert (submit.is_displayed())
            assert (submit.is_enabled())
            submit.click()


    def find_button_2(self):
        with allure.step("Find button 2"):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(demo_locators.ajax_3))
            submit = self.driver.find_element(demo_locators.ajax_3)
            assert (submit.is_displayed())
            assert (submit.is_enabled())
            submit.click()
            time.sleep(2)


    def find_button_3(self):
        with allure.step("Find button 3"):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(demo_locators.button))


    def find_button_4(self):
        with allure.step("Find button 4"):
            self.driver.execute_script("window.scrollBy(0, 2500);")
            time.sleep(1)
            button = self.driver.find_element(demo_locators.button)
            button.click()
            wait = WebDriverWait(self.driver, 10)
            time.sleep(2)


    def find_success_button(self):
        with allure.step("Find success button"):
            success = self.driver.find_element(demo_locators.success)
            assert (success.is_displayed())



