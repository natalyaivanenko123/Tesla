import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.accept_untrusted_certs = True
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
