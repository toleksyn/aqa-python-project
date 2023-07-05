from selene import browser, by, query


class ProductPage:

    def get_product_reviews_count(self):
        return browser.element(by.xpath('(//div[@id="product-summary-header"]//span)[3]')).get(query.text)
