from appium.webdriver.common.appiumby import AppiumBy

from Omelchenko_AppiumTest.AppiumPageObjectClasses.checkout_items_page import CheckoutItemsPage


class NativeCheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def open_checkout_cart_page(self) -> CheckoutItemsPage:
        items_section = self.driver.find_element\
            (AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/orderreview_image_cart']") # com.iherb:id/items_contianer
        items_section.click()
        return CheckoutItemsPage(self.driver)
