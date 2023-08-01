""" Элементы страницы логирования """

import os
from pages.base_page import WebPage
from pages.elements import WebElement, ManyWebElements


class Whois(WebPage):
    """Класс представляющий страницу логирования"""

    def __init__(self, web_driver, url=""):
        if not url:
            url = (
                    os.getenv("WHOIS")
                    or "https://whois.hoster.by/"
            )

        super().__init__(web_driver, url)

    # Инпут ввода поиска
    input_page_whois = WebElement(id="whois_domain")

    # Кнопка поиска
    btn_search_in_whois = WebElement(css_selector='form[id="whois-form"] button[type="submit"]')

    # Таблица результата 1
    result = WebElement(xpath='//div[@class="accent"]/div')

    # Таблица результата 2
    result2 = WebElement(xpath='//div[@class="accent"]//a')

    ################# ПОП АП #################

    btn_pop_up = WebElement(css_selector="[class*='btn'][class*='Fill'].purpBtn")
