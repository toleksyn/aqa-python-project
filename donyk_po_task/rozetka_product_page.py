from selene import browser, by


class ProductPage:

    def verify_product_price_on_product_page(self):
        return browser.element(by.xpath('//p[@class="product-price__big product-price__big-color-red"]')).text
