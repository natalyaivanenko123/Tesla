from selenium.common import NoSuchElementException
from hw_6.pages.base_page import BasePage
from hw_6.pages.locators import auth_locators
import allure
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на страницу авторизации"):
            time.sleep(1)
            self.driver.get("https://auth.tesla.com/oauth2/v1/authorize?redirect_uri=https%3A%2F%2Fwww.tesla.com%2Fteslaaccount%2Fowner-xp%2Fauth%2Fcallback&response_type=code&client_id=ownership&scope=offline_access%20openid%20ou_code%20email%20phone&audience=https%3A%2F%2Fownership.tesla.com%2F&locale=en-US")

    def send_email(self):
        with allure.step("Ввод почты"):
            time.sleep(1)
            self.find_element(auth_locators.input_email).send_keys('natalya-09@mail.ru')

    def send_pass(self):
        with allure.step("Ввод парля"):
            time.sleep(1)
            self.find_element(auth_locators.input_pass).send_keys('1qaz@WSX')

    def click_submit(self):
        time.sleep(1)
        with allure.step("Нажимаем на кнопку входа"):
            self.find_element(auth_locators.form_submit_continue).click()

    def check_dashboard(self):
        time.sleep(1)
        with allure.step("Проверка дашборда"):
            form_dashboard = self.find_element(auth_locators.form_dashboard).is_displayed()
            assert form_dashboard == True
