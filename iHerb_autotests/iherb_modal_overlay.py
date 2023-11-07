from selene import browser, by

from iherbtestvenv.iherb_cart_page import IherbCartPage

class IherbModalOverlay:

    def open_cart_page(self) -> IherbCartPage:
        browser.element(by.xpath('//div[@class="checkout-button"]')).click()
        return IherbCartPage()