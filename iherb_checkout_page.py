from selene import browser, by

class IherbCheckoutPage:

    def get_product_name(self, product_number):
        return browser.element(by.xpath(format('(//div[@class="List__DisplayName-sc-1mvgpt5-4 djMfWv"])[{0}]'\
                                               .format(str(product_number))))).text
