from appium.webdriver.common.appiumby import AppiumBy

from iherb_checkout_items_screen import IherbCheckoutItemsScreen

class IherbNativeCheckoutScreen:
    def __init__(self, driver):
        self.driver = driver

    def open_checkout_cart_screen(self) -> IherbCheckoutItemsScreen:
        items_section = self.driver.find_element\
            (AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/orderreview_image_cart']") # com.iherb:id/items_contianer
        items_section.click()
        return IherbCheckoutItemsScreen(self.driver)