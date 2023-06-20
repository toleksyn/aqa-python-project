from selene import browser, by, be

from Omelchenko_iHerbTest.iherb_checkout_page import IherbCheckoutPage


class IherbCartPage:

    def verify_product_added_to_cart(self):
        browser.element(by.xpath("//div[@data-qa-element='cart-product-list-wrapper']")).should(be.in_dom)

    def open_checkout_page(self) -> IherbCheckoutPage:
        browser.element(by.xpath("//div[@class='css-1ijv08']/a")).click()
        return IherbCheckoutPage()
