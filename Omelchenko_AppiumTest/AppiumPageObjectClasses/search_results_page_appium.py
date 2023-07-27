from appium.webdriver.common.appiumby import AppiumBy
from Omelchenko_AppiumTest.AppiumPageObjectClasses.product_details_page_appium import ProductDetailsPage


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_price(self, product_number):
        return self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/discount_price'])[{0}]"
                            .format(str(product_number))).text

    def open_product_details_page(self, product_number) -> ProductDetailsPage:
        product_card = self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/product_info_item'])[{0}]"
                                           .format(str(product_number)))
        product_card.click()
        return ProductDetailsPage(self.driver)
