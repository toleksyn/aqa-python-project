from appium.webdriver.common.appiumby import AppiumBy
from iherb_returning_customer_screen import IherbRerurningCustomerScreen

class IherbSignFormScreen:
    def __init__(self, driver):
        self.driver = driver

    def tap_sign_in_button(self) -> IherbRerurningCustomerScreen:
        sign_in_button = self.driver.find_element(AppiumBy.XPATH, "//*[@text=' Sign in']")
        sign_in_button.click()
        return IherbRerurningCustomerScreen(self.driver)