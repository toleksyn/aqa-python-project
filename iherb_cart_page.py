from selene import browser, by, be

from pages.iherb_checkout_page import IherbCheckoutPage


class IherbCartPage:
        def verify_that_product_is_added_to_the_cart(self):
        browser.all(by.xpath('//a[@data-qa-element="product-item-title"]')).wait_until(be.visible)

    def procced_to_checkout(self):
        procced_to_checkout_button = browser.element(by.xpath('//a[@data-ga-element="btnToCheckout"]')).click()
        return IherbCheckoutPage()
