from selene import browser, by, be, have

<<<<<<< HEAD
from basket_modal import RozetkaBasketModal
=======
from basket_modal import BasketModal
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71
from product_details_page import ProductDetailsPage

class RozetkaSearchResultsPage:

    def verify_search_results_at_least(self, number_of_results):
        browser.all('//a/span[contains(text(), "")]').should(have.size_greater_than_or_equal(number_of_results))

<<<<<<< HEAD
    def get_product_price(self, product_number):
        return browser.element(by.xpath(format("(//span[@class='goods-tile__price-value'])[{0}]"
                                               .format(str(product_number))))).text

    def get_product_name(self, product_number):
        return browser.element(by.xpath(format("(//span[@class='goods-tile__title'])[{0}]"
                                               .format(str(product_number))))).text

    def add_product_to_basket(self, product_number):
        browser.element(by.xpath("(//app-buy-button/button)[{0}]".format(str(product_number)))).click()
=======
    def verify_product_price_present(self, product_number):
        product = browser.element(by.xpath('//rz-grid/ul/li'))
        product_price_on_search_page = browser.element(by.xpath(
            "(//div[contains(@class, 'goods-tile__inner')])//span[contains(@class, 'goods-tile__price-value')]"))

    def open_the_product(self, product_number):
        product = browser.element(by.xpath('//rz-grid/ul/li'))
        product.should(be.clickable).click()

        return ProductDetailsPage
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71

    def open_product_details_page(self, product_number) -> ProductDetailsPage:
        browser.element(by.xpath(format("(//span[@class='goods-tile__title'])[{0}]".format(str(product_number))))).click()
        return ProductDetailsPage()

    def open_basket_modal(self) -> RozetkaBasketModal:
        browser.element(by.xpath("//rz-cart/button")).click()
        return RozetkaBasketModal()