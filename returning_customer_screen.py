from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile_page_objects.home_page_screen import appium_driver

class ReturningCustomerScreen:
    def __init__(self):
        pass

    def set_username(self, username):
        username_field = appium_driver.find_element(AppiumBy.ID, "username_input")
        username_field.click()
        username_field.send_keys(username)
        appium_driver.execute_script('mobile: performEditorAction', {"action": "type"})
        return self

    def set_password(self, password):
        password_field = appium_driver.find_element(AppiumBy.ID, "Password")
        password_field.click()
        password_field.send_keys(password)
        appium_driver.execute_script('mobile: performEditorAction', {"action": "type"})
        return self

    def submit_the_login_form(self):
        submit_the_login_form_button = appium_driver.find_element(AppiumBy.ID, "sign_in_button")
        submit_the_login_form_button.click()
        return self

    def get_error_text(self):
        error_text = appium_driver.find_element(AppiumBy.XPATH, "//*[@text='Invalid email, phone number, or password']").text
        return error_text