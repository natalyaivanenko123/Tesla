from selenium.webdriver.common.by import By

header_logo = (By.CSS_SELECTOR, "header .tds-site-logo-link")
header_shop_button = (By.CSS_SELECTOR, "header .shop-link")
header_charging_button = (By.CSS_SELECTOR, 'header a[href="/category/charging"]')
header_accessories_button = (By.CSS_SELECTOR, 'header a[href="/category/vehicle-accessories"]')
header_apparel_button = (By.CSS_SELECTOR, 'header a[href="/category/apparel"]')
header_lifestyle_button = (By.CSS_SELECTOR, 'header a[href="/category/lifestyle"]')
header_cart_button = (By.CSS_SELECTOR, 'header .nav-cart')
header_cart_button = (By.CSS_SELECTOR, 'header .nav-cart')
header_menu_button = (By.CSS_SELECTOR, 'header #mobileMenu')

# header = (By.CSS_SELECTOR, ".tds-site-nav-item[data-open-block='tile-1']")
product = (By.CSS_SELECTOR, "*[data-productsku='1669541-00-A']")

quantity_input = (By.CSS_SELECTOR, ".quantity-picker-input input")

add_to_cart_btn = (By.CLASS_NAME, ".submit__buy--desktop.btn-purchasable")

view_cart_button = (By.CLASS_NAME, ".redirect-buttons button.tds-btn--secondary")
checkout_button = (By.CLASS_NAME, ".redirect-buttons button.tds-btn--primary")
