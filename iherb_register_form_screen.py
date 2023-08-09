from appium.webdriver.common.appiumby import AppiumBy
from iherb_returning_customer_screen import IherbReturningCustomerScreen

class IherbSignFormScreen:
    def __init__(self, driver):
        self.driver = driver

    def open_returning_customers_screen(self) -> IherbReturningCustomerScreen:
        sign_in_button = self.driver.find_element(AppiumBy.XPATH, "//*[@text=' Sign in']")
        sign_in_button.click()
        return IherbReturningCustomerScreen(self.driver)