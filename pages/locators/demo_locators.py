from selenium.webdriver.common.by import By

model_s_img = (By.CSS_SELECTOR, ".car-model[data-model='ModelS']")
model_s_img = (By.CSS_SELECTOR, ".car-model[data-model='Model3']")
model_s_img = (By.CSS_SELECTOR, ".car-model[data-model='ModelX']")
model_s_img = (By.CSS_SELECTOR, ".car-model[data-model='ModelY']")

select_model_S_button = (By.CSS_SELECTOR, "button[data-model='ModelS']")
select_model_3_button = (By.CSS_SELECTOR, "button[data-model='Model3']")
select_model_X_button = (By.CSS_SELECTOR, "button[data-model='ModelX']")
select_model_Y_button = (By.CSS_SELECTOR, "button[data-model='ModelY']")

# models = (By.CLASS_NAME, "models")
edit_firstname = (By.ID, "edit-firstname-td")
edit_lastname = (By.ID, "edit-lastname-td")
edit_phonenumber = (By.ID, "edit-phonenumber-td")
edit_usermail = (By.ID, "edit-usermail-td")
edit_zipcode = (By.ID, "edit-zipcode-td")
label = (By.CLASS_NAME, "tds-form-input-choice-label")

demo_submit_button = (By.ID, "edit-submit-td-ajax0")

footer_tesla_link = (By.ID, "footer a[href='/about']")
footer_privacy_link = (By.ID, "footer a[href='/about/legal']")
footer_contact_link = (By.ID, "footer a[href='/contact']")
footer_careers_link = (By.ID, "footer a[href='/careers']")
footer_newsletter_link = (By.ID, "footer a[href='/updates']")
footer_locations_link = (By.ID, "footer a[href='/findus/list']")

# text = (By.CLASS_NAME, "tds-form-feedback-text")
accept_agreement_button = (By.CSS_SELECTOR, ".accept-agreement-btn > .goto-waiver-btn")

# ajax_3 = (By.ID, "edit-submit-td-ajax-3")
complete_later_button = (By.ID, "edit-submit-complete-later")
success_image = (By.CLASS_NAME, "success-image")

add_to_calendar_button = (By.CLASS_NAME, ".add-to-calendar > a")
