from appium.webdriver.common.appiumby import AppiumBy


class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_price(self):
        return self.driver.find_element(AppiumBy.ID, 'com.iherb:id/discounted_price').text

    def get_product_review_amount(self):
        return self.driver.find_element(AppiumBy.ID, 'com.iherb:id/nb_review').text
