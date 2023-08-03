from appium.webdriver.common.appiumby import AppiumBy
from Donyk_Appium_Test.product_screen import ProductScreen
from Donyk_Appium_Test.filter_and_sort_drawer import FilterAndSortDrawer


class SearchResultsScreen:

    def __init__(self, driver):
        self.driver = driver

    def get_product_reviews_count(self, product_number):
        return self.driver.find_element(AppiumBy.XPATH, '(//*[@resource-id="com.iherb:id/rating"])[{0}]'.format(str(product_number))).text

    def open_product_screen(self, product_number):
        product_card = self.driver.find_element(AppiumBy.XPATH, '(//*[@resource-id="com.iherb:id/product_info_item"])[{0}]'.format(str(product_number)))
        product_card.click()
        return ProductScreen(self.driver)

    def open_filter_and_sort_drawer(self):
        filter_and_sort_button = self.driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.iherb:id/productlist_filter_sort_button"]')
        filter_and_sort_button.click()
        return FilterAndSortDrawer(self.driver)

    def get_product_name(self, product_number):
        return self.driver.find_element(AppiumBy.XPATH, '(//*[@resource-id="com.iherb:id/product_info_text"])[{0}]'.format(str(product_number))).text
