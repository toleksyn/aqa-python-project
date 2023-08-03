from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile_page_objects.home_page_screen import appium_driver
from pages.mobile_page_objects.returning_customer_screen import ReturningCustomerScreen

class CreateAnAccountScreen:
    def __init__(self):
        pass

    def sign_in_button_3(self) -> ReturningCustomerScreen:
        button3 = appium_driver.find_element(AppiumBy.XPATH, '//*[@content-desc="Sign in"]')
        button3.click()
        return ReturningCustomerScreen()