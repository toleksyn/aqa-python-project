from appium.webdriver.common.appiumby import AppiumBy

class IherbProductDetailsScreen:
    def __init__(self, driver):
        self.driver = driver

    def get_product_review_amount(self, product_number):
        return self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/nb_review']").text