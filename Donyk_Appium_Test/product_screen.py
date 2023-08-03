from appium.webdriver.common.appiumby import AppiumBy


class ProductScreen:

    def __init__(self, driver):
        self.driver = driver

    def get_product_reviews_count(self):
        return self.driver.find_element(AppiumBy.ID, "com.iherb:id/nb_review").text
