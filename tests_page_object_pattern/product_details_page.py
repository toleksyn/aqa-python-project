<<<<<<< HEAD
from selene import browser, by

class ProductDetailsPage:

    def get_discounted_product_price(self):
        return browser.element(by.xpath("//p[@class='product-price__big product-price__big-color-red']")).text

    def get_original_product_price(self):
        return browser.element(by.xpath("//p[@class='product-price__big']")).text
=======
from selene import browser, by, be, have
from selene import config
import pytest

class ProductDetailsPage:
    def verify_product_price_present_on_pdp(self, product_number):
        price_on_product_page = browser.element(by.xpath('//p[@class="product-price__big product-price__big-color-red"]'))

    def verify_product_name_present(self, product_number):
        name_on_product_page = browser.element(by.xpath("(//div[contains(@class,'goods-tile__inner')])//a[contains(@class,'goods-tile__heading')]/span"))
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71
