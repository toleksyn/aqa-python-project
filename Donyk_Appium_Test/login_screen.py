from appium.webdriver.common.appiumby import AppiumBy
from Donyk_Appium_Test.create_an_account_screen import CreateAnAccountScreen


class LoginScreen:

    def __init__(self, driver):
        self.driver = driver

    def open_create_an_account_screen(self):
        sign_in_button = self.driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.iherb:id/login_page_button_sign_in_with_email"]')
        sign_in_button.click()
        return CreateAnAccountScreen(self.driver)
