from selene import browser, by, have, query


class RozetkaSearchResultsPage:
    def verify_search_results_at_least(self, number_of_results):
        browser.all(by.xpath("//a/span[contains(text(), '')]")).should(have.size_greater_than_or_equal(number_of_results))

    def get_product_price_from_search_result(self, number_of_results):
        all_products = browser.all(by.xpath('//span[@class="goods-tile__price-value"]'))
        product_item = all_products[number_of_results - 1]
        return product_item.get(query.text)

    def open_product_page(self, number_of_results):
        all_product_link = browser.all(
            by.xpath('//div[@class="goods-tile__inner"]//a[contains(., "iPhone")]'))
        product_link = all_product_link[number_of_results - 1]
        product_link.click()
        return RozetkaSearchResultsPage()

    def get_product_name_from_search_result(self, number_of_results):
        all_products = browser.all(by.xpath('//span[contains(text(), "Dell")]'))
        product_item = all_products[number_of_results - 1]
        return product_item.get(query.text)

    def add_product_to_the_cart(self, number_of_results):
        add_icon = browser.all(
            by.xpath('//button[@class="buy-button goods-tile__buy-button ng-star-inserted"]'))
        product_add_icon = add_icon[number_of_results - 1]
        product_add_icon.click()
        return RozetkaSearchResultsPage()

    def open_the_cart_modal(self):
        product_cart_icon = browser.element(by.xpath('//rz-cart'))
        product_cart_icon.click()
        return self
