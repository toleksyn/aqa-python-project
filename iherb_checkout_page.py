from selene import browser, by, query


class IherbCheckoutPage:
    def expand_product_panel(self):
        browser.element(by.xpath('//div[@class="LandingPanel__ToggleText-sc-bh59r1-3 clVDdW"]')).click()
        return IherbCheckoutPage()

    def get_product_name(self):
        browser.all(f'(//div[@class="List__DisplayName-sc-1mvgpt5-4 djMfWv"]').get(query.text)
        return self

