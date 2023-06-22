from selene import browser, by


class ProductPage:

    def get_product_reviews_count(self):
        return browser.element(by.xpath('//a[@class="rating-count"]/span')).text
