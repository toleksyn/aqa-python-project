from selene import browser, by, be, have

from basket_modal import RozetkaBasketModal
from product_details_page import ProductDetailsPage

class RozetkaSearchResultsPage:

    def verify_search_results_at_least(self, number_of_results):
        browser.all('//a/span[contains(text(), "")]').should(have.size_greater_than_or_equal(number_of_results))

    def get_product_price(self, product_number):
        return browser.element(by.xpath(format("(//span[@class='goods-tile__price-value'])[{0}]"
                                               .format(str(product_number))))).text

    def get_product_name(self, product_number):
        return browser.element(by.xpath(format("(//span[@class='goods-tile__title'])[{0}]"
                                               .format(str(product_number))))).text

    def add_product_to_basket(self, product_number):
        browser.element(by.xpath("(//app-buy-button/button)[{0}]".format(str(product_number)))).click()
        return self

    def open_product_details_page(self, product_number) -> ProductDetailsPage:
        browser.element(by.xpath(format("(//span[@class='goods-tile__title'])[{0}]".format(str(product_number))))).click()
        return ProductDetailsPage()

    def open_basket_modal(self) -> RozetkaBasketModal:
        browser.element(by.xpath("//rz-cart/button")).click()
        return RozetkaBasketModal()
