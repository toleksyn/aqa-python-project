from appium.webdriver.common.appiumby import AppiumBy
from Donyk_Appium_Test.returning_customer_screen import ReturningCustomerScreen


class CreateAnAccountScreen:

    def __init__(self, driver):
        self.driver = driver

    def open_returning_customer_screen(self):
        sign_in_button = self.driver.find_element(AppiumBy.XPATH, '//*[@content-desc=" Sign in"]')
        sign_in_button.click()
        return ReturningCustomerScreen(self.driver)
