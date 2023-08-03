from appium.webdriver.common.appiumby import AppiumBy

from Omelchenko_AppiumTest.AppiumPageObjectClasses.cart_page import CartPage


class AddedToCartPopup:
    def __init__(self, driver):
        self.driver = driver

    def open_cart_page(self) -> CartPage:
        view_cart_checkout_button = self.driver.find_element\
            (AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/btn_view_cart']")
        view_cart_checkout_button.click()
        return CartPage(self.driver)
