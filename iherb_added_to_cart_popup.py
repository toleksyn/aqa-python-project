from appium.webdriver.common.appiumby import AppiumBy

from iherb_cart_screen import IherbCartScreen

class IherbAddedToCartPopup:
    def __init__(self, driver):
        self.driver = driver

    def open_cart_screen(self) -> IherbCartScreen:
        view_cart_checkout_button = self.driver.find_element\
            (AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/btn_view_cart']")
        view_cart_checkout_button.click()
        return IherbCartScreen(self.driver)