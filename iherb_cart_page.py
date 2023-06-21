from selene import browser, by

from iherbtestvenv.iherb_checkout_page import IherbCheckoutPage

class IherbCartPage:

    def verify_product_added_to_the_cart(self, product_number):
        browser.element(by.xpath('//div[@data-qa-element="line-item"][{0}]'.\
                                 format(str(product_number)))).click()

    def get_product_name(self, product_number):
         return browser.element(by.xpath(format('(//a[@data-qa-element="product-item-title"])[{0}]'\
                                                .format(str(product_number))))).text

    def proceed_to_checkout(self) -> IherbCheckoutPage:
        browser.element(by.xpath('//a[@data-qa-element="btn-to-checkout"]')).click()
        return IherbCheckoutPage()
