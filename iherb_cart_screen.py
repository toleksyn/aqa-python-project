from appium.webdriver.common.appiumby import AppiumBy

from iherb_checkout_options_drawer import IherbCheckoutOptionsDrawer

class IherbCartScreen:
    def __init__(self, driver):
        self.driver = driver

    def open_checkout_options_drawer(self) -> IherbCheckoutOptionsDrawer:
        checkout_button = self.driver.find_element\
            (AppiumBy.XPATH, "//android.widget.TextView[starts-with(@text, 'Checkout')]")
        checkout_button.click()
        return IherbCheckoutOptionsDrawer(self.driver)