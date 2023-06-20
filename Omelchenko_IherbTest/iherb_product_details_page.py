from selene import browser, by


class IherbProductDetailsPage:

    def get_product_reviews_amount(self):
        return browser.element(by.xpath("//*[@id='product-summary-header']/div[5]/a[2]/span")).text
