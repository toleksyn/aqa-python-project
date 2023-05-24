from selene import browser, by, be, have
from selene import config
import pytest

class BasketModal:

    def verify_basket_modal_title(self):
        browser.element(by.xpath('//h3[@class="modal__heading"]'))

    def verify_close_modal_button(self):
        browser.element(by.xpath('//button[@class="modal__close"]'))

    def verify_product_name_in_basket(self):
        browser.element(by.xpath('//a[@class="cart-product__title"]'))

    def verify_product_price_in_basket(self):
        browser.element(by.xpath('//p[@class="cart-product__price"]'))

    def verify_order_button(self):
        browser.element(by.xpath('//a[@data-testid="cart-receipt-submit-order"]'))