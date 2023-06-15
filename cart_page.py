from selene import browser, by, be, have

from iherbtestvenv.checkout_page import CheckoutPage


class CartPage:

    def verify_that_product_is_to_the_cart(self):
        browser.element(by.xpath('//a [@class="css-1wm8slt"]')).should(be.visible)
        return self()

    def proceed_to_the_checkout_page(self) -> CheckoutPage:
        browser.element(by.xpath('//div[@class="css-1ijv08"]/a')).click()
        return CheckoutPage()