from selene import browser, by

from iherbtestvenv.cart_page import CartPage


class IherbModalContainer:

    def proceed_to_cart_page(self) -> CartPage:
        browser.element(by.xpath('//div[@class="checkout-button"]')).click()
        return CartPage()
