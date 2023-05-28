from selene import browser, by, be, have
from selene import config
import pytest

class ProductDetailsPage:
    def verify_product_price_present_on_pdp(self, product_number):
        price_on_product_page = browser.element(by.xpath('//p[@class="product-price__big product-price__big-color-red"]'))

    def verify_product_name_present(self, product_number):
        name_on_product_page = browser.element(by.xpath("(//div[contains(@class,'goods-tile__inner')])//a[contains(@class,'goods-tile__heading')]/span"))
