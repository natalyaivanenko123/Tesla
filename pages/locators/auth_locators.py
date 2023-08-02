from selenium.webdriver.common.by import By

input_email = (By.ID, "form-input-identity") # Это локатор который отвечает за инпут почты
input_pass = (By.ID, "form-input-credential")
form_submit_continue = (By.ID, "form-submit-continue")
form_dashboard = (By.CSS_SELECTOR, 'ul[class="tds-list styles-module_Navigation__z1jpg"]')

btn_logo = (By.CSS_SELECTOR, 'a[href="https://www.tesla.com/?redirect=no"]')
btn_tesla_2023 = (By.CSS_SELECTOR, 'a[href="https://www.tesla.com/about?redirect=no"]')
btn_privacy_legal = (By.CSS_SELECTOR, 'a[href="https://www.tesla.com/legal/privacy?redirect=no"]')
btn_contact = (By.CSS_SELECTOR, 'a[href="https://www.tesla.com/contact?redirect=no"]')
btn_language_select = (By.ID, "modal-locale-button")
