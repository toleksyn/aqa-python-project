import appium
from pages.mobile_page_objects.sign_in_sign_up_screen import SignInSignUpScreen
from appium.webdriver.common.appiumby import AppiumBy

class MyAccountScreen:
    def __init__(self, driver):
        self.driver = driver

    def open_sign_up_sign_in_account_screen(self) -> SignInSignUpScreen:
        appium.find_element(AppiumBy.ID, 'com.iherb:id/tv_sign_in').click()
        return SignInSignUpScreen()
