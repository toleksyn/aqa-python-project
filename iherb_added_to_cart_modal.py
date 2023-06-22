from selene import browser, by

from pages.iherb_cart_page import IherbCartPage


class IherbAddedToCartModal:
    def open_the_cart_page(self):
        view_cart_button = browser.element(by.xpath('//div[@class="checkout-button"]')).click()
        return IherbCartPage()
