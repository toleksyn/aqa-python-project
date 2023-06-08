from selene import browser, by, have

from Omelchenko_RozetkaPageObjectTest.rozetka_cart_popup import RozetkaCartPopup
from Omelchenko_RozetkaPageObjectTest.rozetka_product_description_page import RozetkaProductDescriptionPage


class RozetkaSearchResultsPage:

    def verify_search_results_have_size_at_least(self, page_size):
        browser.all(by.xpath("//a/span[@class ='goods-tile__title']")).should(have.size_at_least(page_size))

    def get_product_price(self, product_number):
        return browser.element(by.xpath(format("(//span[@class='goods-tile__price-value'])[{0}]"
                                               .format(str(product_number))))).text

    def get_product_name(self, product_number):
        return browser.element(by.xpath(format("(//span[@class='goods-tile__title'])[{0}]"
                                               .format(str(product_number))))).text

    def add_to_cart(self, product_number) -> RozetkaCartPopup:
        browser.element(by.xpath("(//app-buy-button/button)[{0}]".format(str(product_number)))).click()
        return RozetkaCartPopup()

    def open_product_description_page(self, product_number) -> RozetkaProductDescriptionPage:
        browser.element(by.xpath("(//span[@class='goods-tile__title'])[{0}]".format(str(product_number)))).click()
        return RozetkaProductDescriptionPage()

    def open_cart_popup(self) -> RozetkaCartPopup:
        browser.element(by.xpath("//rz-cart/button")).click()
        return RozetkaCartPopup()
