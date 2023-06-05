from selene import browser, by


class ProductPage:

    def get_product_price(self, product_number):
        return browser.element(by.xpath('(//p[@class="product-price__big product-price__big-color-red"])[{0}]'.format(str(product_number)))).text
