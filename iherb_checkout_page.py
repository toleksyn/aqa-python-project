from selene import browser, by, query


class IherbCheckoutPage:
    def expand_product_panel(self):
        browser.element(by.xpath('//div[@class="LandingPanel__ToggleText-sc-bh59r1-3 clVDdW"]')).click()
        return IherbCheckoutPage()

    def get_product_name_from_checkout(self):
        browser.all(f'(//div[contains(text(),"")])').get(query)
        return query

