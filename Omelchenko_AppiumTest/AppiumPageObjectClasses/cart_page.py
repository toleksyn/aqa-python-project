from appium.webdriver.common.appiumby import AppiumBy

from Omelchenko_AppiumTest.AppiumPageObjectClasses.checkout_options_drawer import CheckoutOptionsDrawer


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        
    def open_checkout_options_drawer(self) -> CheckoutOptionsDrawer:
        checkout_button = self.driver.find_element\
            (AppiumBy.XPATH, "//android.widget.TextView[starts-with(@text, 'Checkout')]")
        checkout_button.click()
        return CheckoutOptionsDrawer(self.driver)
