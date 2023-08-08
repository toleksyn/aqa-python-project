from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile_page_objects.home_page_screen import appium_driver
from pages.mobile_page_objects.returning_customer_screen import ReturningCustomerScreen

class CreateAnAccountScreen:
    def __init__(self, driver):
        self.driver = driver

    def open_returning_customer_screen(self) -> ReturningCustomerScreen:
        sign_up_sign_in_button = appium_driver.find_element(AppiumBy.XPATH, '//*[@content-desc="Sign in"]')
        sign_up_sign_in_button.click()
        return ReturningCustomerScreen()
