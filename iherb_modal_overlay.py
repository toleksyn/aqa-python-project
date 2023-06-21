from selene import browser, by, be

from iherbtestvenv.iherb_cart_page import IherbCartPage

class IherbModalOverlay:

    def verify_modal_open(self):
        browser.element(by.xpath('//div[@class="iherb-modal-overlay"]')).should(be.visible)

    def open_cart_page(self) -> IherbCartPage:
        browser.element(by.xpath('//div[@class="checkout-button"]')).click()
        return IherbCartPage()
