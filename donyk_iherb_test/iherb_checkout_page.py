from selene import browser, by


class CheckoutPage:

    def get_product_name(self):
        return browser.element(by.xpath('//div[@class="List__DisplayName-sc-1mvgpt5-4 djMfWv"]')).text
