from selene import browser, by

class ProductDetailsPage:

    def get_product_review_on_details_page(self):
        return browser.element(by.xpath('//*[@id="product-summary-header"]/div[5]/a[2]/span'))