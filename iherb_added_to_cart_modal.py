from selene import browser, by

from pages.iherb_cart_page import IherbCartPage


class IherbCartModal:
    def open_the_cart_page(self):
        browser.element(by.xpath('//div[@class="checkout-button"]')).click()
        return IherbCartPage()
