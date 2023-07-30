import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hw_6.pages.locators import demo_locators

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

driver.maximize_window()
# Открытие страницы
driver.get("https://www.tesla.com/drive")

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)

wait.until(demo_locators.models)

models = driver.find_elements(demo_locators.models)
for item in models:
    ActionChains(driver).move_to_element(item).perform()
    assert(item.is_displayed())
    assert(item.is_enabled())

models[0].click()
assert(models[0])

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)

input = driver.find_element(demo_locators.edit_firstname)
input.send_keys("Natalja")

input = driver.find_element(demo_locators.edit_lastname)
input.send_keys("Ivanenko")

input = driver.find_element(demo_locators.edit_phonenumber)
input.send_keys("2015550123")

input = driver.find_element(demo_locators.edit_usermail)
input.send_keys("hello@mail.ru")

input = driver.find_element(demo_locators.edit_zipcode)
input.send_keys("78585")

driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)

terms = driver.find_element(demo_locators.label)
#ActionChains(driver).move_to_element(terms).perform()
terms.click()

errors = driver.find_elements(demo_locators.text)
for error in errors:
    assert(not error.is_displayed())

submit = driver.find_element(demo_locators.ajax0)
assert(submit.is_displayed())
assert(submit.is_enabled())
submit.click()


wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located(demo_locators.ajax_3))

submit = driver.find_element(demo_locators.ajax_3)
assert(submit.is_displayed())
assert(submit.is_enabled())
submit.click()

time.sleep(2)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located(demo_locators.button))

driver.execute_script("window.scrollBy(0, 2500);")
time.sleep(1)

button = driver.find_element(demo_locators.button)
button.click()

wait = WebDriverWait(driver, 10)
time.sleep(2)

success = driver.find_element(demo_locators.success)
assert(success.is_displayed())


time.sleep(2)

# Закрытие браузера
driver.quit()