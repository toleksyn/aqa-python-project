from selene import browser, by, query

class IherbProductDetailsPage:
    def get_reviews_count_from_product_page(self):
        return browser.element(by.xpath("//a[@class='rating-count']/span")).get(query.inner_html)
