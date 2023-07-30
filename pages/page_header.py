# from selenium.common import NoSuchElementException
# from hw_6.pages.base_page import BasePage
# from hw_6.pages.locators import header_locators
# import allure
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
#
# class HeaderPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     def open(self):
#         with allure.step("Перейти на страницу"):
#             self.driver.get("https://www.tesla.com/")
#             wait = WebDriverWait(self.driver, 10)
#
#     def test_header(self):
#         with allure.step("Test_header"):
#             self.is_element_present(header_locators.header)
#
#     def find_and_check_buttons(self):
#         with allure.step("Find and check buttons"):
#             buttons = self.find_elements(header_locators.header_btn)
#             for item in buttons:
#                 ActionChains(self.driver).move_to_element(item).perform()
#                 assert (item.is_displayed())
#                 buttons[0].click()
#                 assert (buttons[0])
#     def find_element(header_locators.header_logo)
#         with allure.step("Find and check buttons"):
#             ActionChains(self.driver).move_to_element(logo).perform()
#             assert(logo.is_displayed())