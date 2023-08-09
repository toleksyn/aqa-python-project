from appium.webdriver.common.appiumby import AppiumBy

from iherb_native_checkout_screen import IherbNativeCheckoutScreen

class IherbCheckoutOptionsDrawer:
    def __init__(self, driver):
        self.driver = driver

    def open_checkout_screen(self) -> IherbNativeCheckoutScreen:
        checkout_button = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/checkout_tv']")
        checkout_button.click()
        return IherbNativeCheckoutScreen(self.driver)