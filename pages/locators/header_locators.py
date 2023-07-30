from selenium.webdriver.common.by import By

header = (By.ID, 'tds-site-header')

logo = (By.CLASS_NAME, 'header tds-site-logo-link')

model_s = (By.CSS_SELECTOR, 'a[href="/models"]')
model_3 = (By.CSS_SELECTOR, 'a[href="/model3"]')
model_x = (By.CSS_SELECTOR, 'a[href="/modelx"]')
model_y = (By.CSS_SELECTOR, 'a[href="/modely"]')
model_solar_roof = (By.CSS_SELECTOR, 'a[href="/solarroof"]')
model_solar_panels = (By.CSS_SELECTOR, 'a[href="/solarpanels"]')
model_solar_powerwall = (By.CSS_SELECTOR, 'a[href="/powerwall"]')

shop_button = (By.CSS_SELECTOR, 'a[href="https://shop.tesla.com"]')
account_button = (By.CSS_SELECTOR, 'a[href="/teslaaccount"]')
menu_button = (By.CSS_SELECTOR, 'button[action="secondaryNavigationItems"]')
