from selene import browser, by, have
from rozetka_product_page import ProductPage
from rozetka_cart_popup import CartPopup


class SearchResultsPage:

    def verify_search_results_at_least(self, number_of_results):
        browser.all(by.xpath('//a/span[contains(text(),"")]')).should(have.size_at_least(number_of_results))

    def verify_product_price(self, product_number):
        return browser.element(by.xpath(format('(//span[@class="goods-tile__price-value"])[{0}]'.format(str(product_number))))).text

    def open_product_page(self, product_number):
        browser.element(by.xpath('//div[@data-goods-id="352486566"]')).click()
        return ProductPage

    def verify_product_name(self, product_number):
        return browser.element(by.xpath(format('(//span[@class="goods-tile__title"])[{0}]'.format(str(product_number))))).text

    def add_product_to_cart(self, product_number):
        browser.element(by.xpath('(//button[@class="buy-button goods-tile__buy-button ng-star-inserted"])[{0}]'.format(str(product_number)))).click()

    def open_cart_popup(self) -> CartPopup:
        browser.element(by.xpath('//button[@class="header__button ng-star-inserted header__button--active"]')).click()
        return CartPopup()
