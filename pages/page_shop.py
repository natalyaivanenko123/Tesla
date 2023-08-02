from selenium.common import NoSuchElementException
from natalya_ivanenko.hw_6.pages.base_page import BasePage
from natalya_ivanenko.hw_6.pages.locators import shop_locators
import allure


class ShopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get("https://shop.tesla.com/")

    def find_header(self):
        with allure.step("Find header"):
            button = self.find_element(shop_locators.header)
            button.click()

    def find_product(self):
        with allure.step("Find product"):
            product = self.find_element(shop_locators.product)
            product.click()

    def find_purchasable(self):
        with allure.step("Find purchasable"):
            button = self.find_element(shop_locators.btn_purchasable)
            button.click()
    def go_to_cart(self):
        with allure.step("Go to cart"):
            self.driver.get("https://shop.tesla.com/cart")

    def find_checkout(self):
        with allure.step("Find checkout"):
            button = self.find_element(shop_locators.checkout)
            assert self.is_element_visible(button)
            assert self.is_element_enabled(button)
            button.click()
