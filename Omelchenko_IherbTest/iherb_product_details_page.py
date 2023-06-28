from selene import browser, by, query


class IherbProductDetailsPage:

    def get_product_reviews_amount(self):
        return browser.element(by.xpath("(//*[@id='product-summary-header']//span)[3]")).get(query.text)
