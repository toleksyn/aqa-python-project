from selene import browser, by

from iherbtestvenv.iherb_payment_update_page import IherbPaymentUpdatePage

class IherbOrderReviewInPage:

    def place_order_with_incorrect_card_number(self) -> IherbPaymentUpdatePage:
        browser.element(by.xpath('//button[@data-testid="place-order-button"]')).click()
        return IherbPaymentUpdatePage()
