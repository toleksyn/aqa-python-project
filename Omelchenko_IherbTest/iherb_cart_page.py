from selene import browser, by, query

from Omelchenko_iHerbTest.iherb_checkout_page import IherbCheckoutPage
from Omelchenko_iHerbTest.iherb_login_landing_page import IherbLoginLandingPage


class IherbCartPage:

    def open_checkout_page_while_logged_in(self) -> IherbCheckoutPage:
        browser.element(by.xpath("//div[@class='css-1ijv08']/a")).click()
        return IherbCheckoutPage()

    def open_checkout_page_while_not_logged_in(self) -> IherbLoginLandingPage:
        browser.element(by.xpath("//div[@class='css-1ijv08']/a")).click()
        return IherbLoginLandingPage()

    def get_product_name(self, product_number):
        return browser.element(by.xpath("(//div[@class='css-1bn574b']/a)[{0}]"
                                        .format(str(product_number)))).get(query.text)

    def get_product_price(self, product_number):
        return browser.element(by.xpath("(//div[@class='css-1yxu09j'])[{0}]"
                                        .format(str(product_number)))).get(query.text)
