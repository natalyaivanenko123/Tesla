import allure, time
from pages.domain.whois import Whois
import pytest_check as check


def check_element(element):
    return check.is_true(element.is_visible()) or check.is_true(element.is_clickable())


@allure.feature('Whois')
@allure.story('Проверка регистрации домена')
def test_page_whois_hoster(web_browser):
    """ Проверяем функционала whois """

    page = Whois(web_browser)

    page.btn_pop_up.click()

    with allure.step("Проверка регистрации домена"):
        with allure.step("Нажатие и ввод имени сайта"):
            page.input_page_whois.send_keys('anatoly.site')

        with allure.step("Нажатие на кнопку поиска"):
            page.btn_search_in_whois.click()
            time.sleep(3)

        text = page.result.get_text()
        text_list = text.split("\n")

        with allure.step("Результаты проверки домена"):
            check.equal(text_list[3], "Registrar URL: https://hoster.by")

    with allure.step("Проверка не зарегистрированного домена в hoster"):
        with allure.step("Ввод имени сайта для поиска"):
            page.input_page_whois.send_keys_all_select("google.com")

        with allure.step("Нажатие на кнопку поиска"):
            page.btn_search_in_whois.click()
            time.sleep(3)

        text = page.result.get_text()
        text_list = text.split("\n")

        with allure.step("Результаты проверки домена"):
            check.equal(text_list[3], "Registrar URL: http://www.markmonitor.com")

    with allure.step("Проверка регистрации домена"):
        with allure.step("Ввод имени сайта для поиска"):
            page.input_page_whois.send_keys_all_select("pkopnefgkongofewqg")

        with allure.step("Нажатие на кнопку поиска"):
            page.btn_search_in_whois.click()
            time.sleep(3)

        with allure.step("Результаты проверки домена"):
            check.is_true(page.result2.is_clickable(), "Доменное имя не доступно для регистрации")
