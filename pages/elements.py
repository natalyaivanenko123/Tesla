import time
from termcolor import colored
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class WebElement(object):
    _locator = ('', '')
    _web_driver = None
    _page = None
    _timeout = 10
    _wait_after_click = False

    def __init__(self, timeout=10, wait_after_click=False, **kwargs):
        self._timeout = timeout
        self._wait_after_click = wait_after_click

        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def find(self, timeout=10):
        """ Найти элемент на странице. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.presence_of_element_located(self._locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))

        return element

    def wait_to_be_clickable(self, timeout=10, check_visibility=True):
        """ Подождите, пока элемент будет готов к клику. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator)
            )
        except:
            print(colored('Element not clickable!', 'red'))

        if check_visibility:
            self.wait_until_not_visible()

        return element

    def wait_for_visibility(self, timeout=10):
        """ Подождите, пока элемент не станет видимым на странице. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
        except:
            print(colored('Element not visible!', 'red'))

        return element

    def is_clickable(self):
        """ Проверить, готов ли элемент к клику или нет. """

        element = self.wait_to_be_clickable(timeout=1)
        return element is not None

    def is_presented(self):
        """ Убедитесь, что элемент представлен на странице. """

        element = self.find(timeout=1)
        return element is not None

    def is_visible(self):
        """ Проверить, виден элемент или нет. """

        element = self.find(timeout=1)

        if element:
            return element.is_displayed()

        return False

    def send_keys(self, keys, wait=2):
        """ Отправить ключи к элементу. """

        keys = keys.replace('\n', '\ue007')

        element = self.find()

        if element:
            element.click()
            element.clear()
            element.send_keys(keys)
            time.sleep(wait)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def send_keys_all_select(self, keys, wait=2):
        """ Отправить ключи к элементу второй вариант. """

        keys = keys.replace('\n', '\ue007')

        element = self.find()

        if element:
            element.click()
            element.send_keys(Keys.CONTROL + 'a')
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(keys)
            time.sleep(wait)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def get_text(self):
        """ Получить текст элемента. """

        element = self.find()
        text = ''

        try:
            text = str(element.text)
        except Exception as e:
            print('Error: {0}'.format(e))

        return text

    def get_attribute(self, attr_name):
        """ Получить атрибут элемента. """

        element = self.find()

        if element:
            return element.get_attribute(attr_name)

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        """ Подождать и кликнуть по элементу. """

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()

    def move_to(self, x_offset=0, y_offset=0, hold_seconds=0):
        """ Наведение мышки на элемент без клика """

        element = self.find()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).pause(1).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))


class ManyWebElements(WebElement):

    def __getitem__(self, item):
        """ Получить список элементов и попытаться вернуть требуемый элемент. """

        elements = self.find()
        return elements[item]

    def find(self, timeout=10):
        """ Поиск элементов на странице. """

        elements = []

        try:
            elements = WebDriverWait(self._web_driver, timeout).until(
                EC.presence_of_all_elements_located(self._locator)
            )
        except:
            print(colored('Elements not found on the page!', 'red'))

        return elements
