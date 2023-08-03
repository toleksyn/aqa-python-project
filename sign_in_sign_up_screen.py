from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile_page_objects.create_an_account import CreateAnAccountScreen
from pages.mobile_page_objects.home_page_screen import appium_driver

class SignInSignUpScreen:
    def __init__(self):
        pass

    def sign_in_button_2(self) -> CreateAnAccountScreen:
        button2 = appium_driver.find_element(AppiumBy.ID, 'com.iherb:id/login_page_button_sign_in_with_email')
        button2.click()
        return CreateAnAccountScreen()