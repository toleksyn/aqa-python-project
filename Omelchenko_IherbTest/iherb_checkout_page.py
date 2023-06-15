from selene import browser
from selene.support import by


class IherbCheckoutPage:

    def get_product_name(self):
        return browser.element(by.xpath("//div[@class='List__DisplayName-sc-1mvgpt5-4 djMfWv']")).text
