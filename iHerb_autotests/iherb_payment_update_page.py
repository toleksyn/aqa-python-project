from selene import browser, by, be

from iherbtestvenv.iherb_order_details_page import IherbOrderDetailsPage

class IherbPaymentUpdatePage:

    def verify_displaying_order_summary_button(self):
        return browser.element(by.xpath('//div[@class="css-kvi0m9"]')).should(be.visible)

    def navigate_to_order_summary_page(self) -> IherbOrderDetailsPage:
        browser.element(by.xpath('//div[@class="css-kvi0m9"]')).click()
        return IherbOrderDetailsPage()