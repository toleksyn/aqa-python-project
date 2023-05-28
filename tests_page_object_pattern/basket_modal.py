from selene import browser, by, be, have
from selene import config
import pytest

class BasketModal:

    def verify_that_basket_modal_is_open(self):
        browser.element(by.xpath("//rz-cart/button")).click()

    def verify_product_name_in_basket(self):
        browser.element(by.xpath('//div[@class="cart-product__main"]/a')).should(be.existing).text

    def verify_product_price_in_basket(self):
        browser.element(by.xpath('//p[@class="cart-product__price"]')).should(be.existing).text

    def verify_order_button(self):
        browser.element(by.xpath('//a[@data-testid="cart-receipt-submit-order"]')).should(be.existing)

        return BasketModal