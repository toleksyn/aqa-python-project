from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile_page_objects.home_page_screen import appium_driver
from pages.mobile_page_objects.product_details_screen import ProductDetailsScreen

class SearchResultsScreen:
    def __init__(self, driver):
        self.driver = driver

    def verify_search_results_at_least(self, number_of_search_results):
        search_results_count = appium_driver.find_element(AppiumBy.ID, 'com.iherb:id/productlist_productcount_textview').text
        actual_search_results_count = len(search_results_count)
        assert actual_search_results_count >= number_of_search_results, f"Search results count is less than 5"
        return SearchResultsScreen

    def get_product_price_from_search_serults(self, product_number):
        return appium_driver.find_element(AppiumBy.XPATH, f"(//*[@resource-id='com.iherb:id/discount_price'])[{product_number}]").text

    def open_product_details_screen(self, product_number) -> ProductDetailsScreen:
        product_card = appium_driver.find_element(AppiumBy.XPATH, f"(//*[@resource-id='com.iherb:id/product_info_item'])[{product_number}]")
        product_card.click()
        return ProductDetailsScreen()

    def open_filter_and_sort_drawer(self):
        filter_and_sort_button = self.driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.iherb:id/productlist_filter_sort_button"]')
        filter_and_sort_button.click()
        return FilterAndSortDrawer(self.driver)

    def get_product_name(self, product_number):
        return self.driver.find_element(AppiumBy.XPATH, '(//*[@resource-id="com.iherb:id/product_info_text"])[{0}]'.format(str(product_number))).text
