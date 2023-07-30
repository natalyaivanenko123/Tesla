import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hw_6.pages.locators import shop_locators

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

driver.maximize_window()
# Открытие страницы
driver.get("https://shop.tesla.com/")

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
time.sleep(2)

button = driver.find_element(shop_locators.header)
button.click()

time.sleep(2)
product = driver.find_element(shop_locators.product)
product.click()

time.sleep(2)
button = driver.find_element(shop_locators.btn_purchasable)
button.click()

time.sleep(2)

driver.get("https://shop.tesla.com/cart")


button = driver.find_element(shop_locators.checkout)
assert(button.is_displayed())
assert(button.is_enabled())
button.click()

wait = WebDriverWait(driver, 10)
time.sleep(2)

assert(driver.current_url == "https://shop.tesla.com/login?checkoutFlow=true")

time.sleep(2)

driver.quit()