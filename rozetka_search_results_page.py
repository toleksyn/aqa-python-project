from selene import browser, by, have, be


class RozetkaSearchResultsPage:
    def verify_search_results_at_least(self, number_of_results):
        browser.all(by.xpath("//a/span[contains(text(), 'iPhone')]")).should(
            have.size_greater_than_or_equal(number_of_results))
        return self

    def get_price_from_search_result(self, number_of_results):
        browser.element(by.xpath('//span[@class="goods-tile__price-value"]'))\
            .should(be.visible)
        return self

    def open_product_number_three(self, number_of_results):
        product_link = browser.element(by.xpath('//div[@class="goods-tile__inner"]//a[contains(., "iPhone")]'))
        product_link.should(be.clickable).click()
        return RozetkaSearchResultsPage()
    


