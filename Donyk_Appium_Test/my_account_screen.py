from appium.webdriver.common.appiumby import AppiumBy
from Donyk_Appium_Test.login_screen import LoginScreen


class MyAccountScreen:

    def __init__(self, driver):
        self.driver = driver

    def open_login_screen(self):
        sign_in_button = self.driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.iherb:id/tv_sign_in"]')
        sign_in_button.click()
        return LoginScreen(self.driver)
