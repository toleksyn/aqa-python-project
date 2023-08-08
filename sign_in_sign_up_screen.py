from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile_page_objects.create_an_account import CreateAnAccountScreen
from pages.mobile_page_objects.home_page_screen import appium_driver

class SignInSignUpScreen:
    def __init__(self, driver):
        self.driver = driver

    def open_create_account_screen(self) -> CreateAnAccountScreen:
        sign_in_slash_sign_in_button = appium_driver.find_element(AppiumBy.ID, 'com.iherb:id/login_page_button_sign_in_with_email')
        sign_in_slash_sign_in_button.click()
        return CreateAnAccountScreen()
