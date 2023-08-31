from appium.webdriver.common.appiumby import AppiumBy

from Omelchenko_AppiumTest.AppiumPageObjectClasses.added_to_cart_popup import AddedToCartPopup
from Omelchenko_AppiumTest.AppiumPageObjectClasses.filter_and_sort_drawer import FilterAndSortDrawer
from Omelchenko_AppiumTest.AppiumPageObjectClasses.product_details_page import ProductDetailsPage


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_price(self, product_number):
        return self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/discount_price'])[{0}]"
                            .format(str(product_number))).text

    def open_product_details_page(self, product_number) -> ProductDetailsPage:
        product_card = self.driver.find_element\
            (AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/product_info_item'])[{0}]".format(str(product_number)))
        product_card.click()
        return ProductDetailsPage(self.driver)

    def get_product_review_amount(self, product_number):
        return self.driver.find_element\
            (AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/rating'])[{0}]".format(str(product_number))).text

    def verify_that_search_results_have_size_at_least(self, expected_product_amount):
        products_amount = self.driver.find_element\
            (AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/productlist_productcount_textview']").text
        actual_product_amount = products_amount.replace(' Results', '')
        assert int(actual_product_amount) > expected_product_amount, \
            f'Search results amount less than {expected_product_amount}'

    def open_filter_and_sort_drawer(self) -> FilterAndSortDrawer:
        filter_and_sort_button = self.driver.find_element\
            (AppiumBy.ID,"com.iherb:id/productlist_filter_sort_button")
        filter_and_sort_button.click()
        return FilterAndSortDrawer(self.driver)

    def get_product_name(self, product_number):
        return self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/product_info_text'])[{0}]"
                                        .format(str(product_number))).text

    def add_to_cart(self, product_number) -> AddedToCartPopup:
        add_to_cart_button = self.driver.find_element\
            (AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/add_cart_icon'])[{0}]".format(str(product_number)))
        add_to_cart_button.click()
        return AddedToCartPopup(self.driver)
