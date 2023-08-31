from appium.webdriver.common.appiumby import AppiumBy


class CheckoutItemsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_full_product_name(self, product_number):
        return self.get_product_brand(product_number) + ', ' + self.get_product_name(product_number)

    def get_product_brand(self, product_number):
        return self.driver.find_element\
            (AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/checkoutcart_productitem_brandname'])[{0}]"
             .format(str(product_number))).text

    def get_product_name(self, product_number):
        return self.driver.find_element\
            (AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/checkoutcart_productitem_productname'])[{0}]"
             .format(str(product_number))).text
