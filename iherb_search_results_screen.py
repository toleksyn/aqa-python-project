from appium.webdriver.common.appiumby import AppiumBy
from iherb_product_details_screen import IherbProductDetailsScreen
from iherb_filter_and_sorter_drawer import IherbFilterAndSorterDrawer

class IherbSearchResultsScreen:
    def __init__(self, driver):
        self.driver = driver

    def get_product_price(self, product_number):
        return self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/discount_price'])[{0}]"
                            .format(str(product_number))).text

    def open_product_details_page(self, product_number) -> IherbProductDetailsScreen:
        product_card = self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/product_info_item'])[{0}]"
                                           .format(str(product_number))).text
        product_card.click()
        return IherbProductDetailsScreen(self.driver)

    def get_product_review_amount(self, product_number):
        return self.driver.find_element(AppiumBy.XPATH, "(//*[resource-id='com.iherb:id/rating'])[{0]").format(str(product_number)).text

    def verify_that_search_results_have_size_at_least(self, expected_product_amount):
        products_amount = self.driver.find_element(AppiumBy.XPATH, "//*[resource-id='com.iherb:id/productlist_productcount_textreview']").text
        actual_sesult_amount = products_amount.replace(' Results', '')
        assert int(actual_sesult_amount) > expected_product_amount, \
            f'Search results amount less than {expected_product_amount}'

    def open_filter_and_sort_drawer(self) -> IherbFilterAndSorterDrawer:
        filter_and_sort_button = self.driver.find_element(AppiumBy.ID, "com.iherb:id/productlist_filter_sort_button")
        filter_and_sort_button.click()
        return IherbFilterAndSorterDrawer(self.driver)

    def get_product_name(self, product_number):
        return self.driver.find_element(AppiumBy.XPATH, "(//*[resource-id='com.iherb:id/product_info_text'])[{0}]").format(str(product_number)).text
