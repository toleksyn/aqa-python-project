from selene import browser, by, be, have
from selene import config
import pytest

from basket_modal import BasketModal
from product_details_page import ProductDetailsPage

class RozetkaSearchResultsPage:

    def verify_search_results_at_least(self, number_of_results):
        browser.all('//a/span[contains(text(), "")]').should(have.size_greater_than_or_equal(number_of_results))

    def verify_product_price_present(self, product_number):
        product = browser.element(by.xpath('//rz-grid/ul/li'))
        product_price_on_search_page = browser.element(by.xpath(
            "(//div[contains(@class, 'goods-tile__inner')])//span[contains(@class, 'goods-tile__price-value')]"))

    def open_the_product(self, product_number):
        product = browser.element(by.xpath('//rz-grid/ul/li'))
        product.should(be.clickable).click()

        return ProductDetailsPage

    def add_products_to_basket(self, product_number):
        browser.element(by.xpath("(//div[@class='goods-tile__inner']//button[contains(@class, 'buy-button')])")).click()

        return BasketModal()