from selene import browser, by


class CartPopup:

    def save_product_name(self):
        return browser.element(by.xpath('//a[@class="cart-product__title"]')).text

    def save_product_price(self):
        return browser.element(by.xpath('//p[@class="cart-product__price"]')).text
