from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile_page_objects.preferences_screen import appium_driver

class ProductDetailsScreen:
    def __init__(self, driver):
        self.driver = driver

    def get_product_price_from_product_details_screen(self):
        return appium_driver.find_element(AppiumBy.ID, 'com.iherb:id/discounted_price').text
