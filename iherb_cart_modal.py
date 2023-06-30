from selene import browser, by, query
from pages.iherb_cart_page import IherbCartPage

class IherbCartModal:
    def open_the_cart_page(self):
        browser.element(by.xpath('//div[@class="checkout-button"]')).click()
        return IherbCartPage()

    def get_product_name(self):
        browser.element(by.xpath('f(//div[@class="product-name "])')).get(query.text)
        return IherbCartModal()
