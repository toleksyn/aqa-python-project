from selene import browser, by, query

class IherbProductDetailsPage:

    def get_product_reviews_amount(self):
        return browser.element(by.xpath("//div[@id='product-summary-header']//a[2]/span")).get(query.text)
