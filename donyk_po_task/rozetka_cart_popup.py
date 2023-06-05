from selene import browser, by


class CartPopup:

    def get_product_name(self, product_number):
        return browser.element(by.xpath('(//a[@class="cart-product__title"])[{0}]'.format(str(product_number)))).text

    def get_product_price(self, product_number):
        return browser.element(by.xpath('(//p[@class="cart-product__price cart-product__price--red"])[{0}]'.format(str(product_number)))).text

