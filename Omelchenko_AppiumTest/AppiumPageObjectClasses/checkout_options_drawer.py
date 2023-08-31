from appium.webdriver.common.appiumby import AppiumBy

from Omelchenko_AppiumTest.AppiumPageObjectClasses.native_checkout_page import NativeCheckoutPage


class CheckoutOptionsDrawer:
    def __init__(self, driver):
        self.driver = driver

    def open_checkout_page(self) -> NativeCheckoutPage:
        checkout_button = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/checkout_tv']")
        checkout_button.click()
        return NativeCheckoutPage(self.driver)
