from selene import browser, by, query


class CheckoutPage:

    def get_product_name(self):
        return browser.element(by.xpath('//div[@class="List__DisplayName-sc-1mvgpt5-4 djMfWv"]')).get(query.text)

    def place_order(self):
        browser.element(by.xpath('//button[@id="place-order-button"]')).click()
        from iherb_update_payment_page import UpdatePaymentPage
        return UpdatePaymentPage()
