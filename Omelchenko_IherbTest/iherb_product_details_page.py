from selene import browser, by


class IherbProductDetailsPage:

    def get_product_reviews_amount(self):
        return browser.element(by.xpath("(//div[@id='product-summary-header']/div[4]/a[2]/span)")).text
