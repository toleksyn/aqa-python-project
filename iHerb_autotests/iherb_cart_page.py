from selene import browser, by, query

from iherbtestvenv.iherb_checkout_page import IherbCheckoutPage

class IherbCartPage:

    def verify_product_added_to_the_cart(self, product_number):
        browser.element(by.xpath('//div[@data-qa-element="line-item"][{0}]'.\
                                 format(str(product_number)))).click()

    def get_product_name(self, product_number):
        return browser.element(by.xpath("(//div[@class='css-1bn574b']/a)[{0}]"
                                        .format(str(product_number)))).get(query.text)

    def proceed_to_checkout(self) -> IherbCheckoutPage:
        browser.element(by.xpath('//a[@data-qa-element="btn-to-checkout"]')).click()
        return IherbCheckoutPage()

    def get_product_name(self, product_number):
        return browser.element(by.xpath("(//div[@class='css-1bn574b']/a)[{0}]"
                                        .format(str(product_number)))).get(query.text)

    def get_product_price(self, product_number):
        return browser.element(by.xpath("(//div[@class='css-1yxu09j'])[{0}]"
                                        .format(str(product_number)))).get(query.text)