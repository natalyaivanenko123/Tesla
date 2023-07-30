import pytest
from natalya_ivanenko.hw_6.pages.page_shop import ShopPage
from natalya_ivanenko.hw_6.pages.page_demo import DemoPage
import allure


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Purchase")
@allure.title("Random product")
def test_shop(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.find_header()
    shop_page.find_product()
    shop_page.find_purchasable()
    shop_page.go_to_cart()
    shop_page.find_checkout()
def test_demo(driver):
    demo_page = DemoPage(driver)
    demo_page.open()
    demo_page.find_and_check_models()
    demo_page.fill_form()
    demo_page.find_label()
    demo_page.check_errors()
    demo_page.find_button_1()
    demo_page.find_button_2()
    demo_page.find_button_3()
    demo_page.find_button_4()
    demo_page.find_success_button()