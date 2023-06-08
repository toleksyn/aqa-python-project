from selene import browser, by

class ProductDetailsPage:

    def get_discounted_product_price(self):
        return browser.element(by.xpath("//p[@class='product-price__big product-price__big-color-red']")).text

    def get_original_product_price(self):
        return browser.element(by.xpath("//p[@class='product-price__big']")).text