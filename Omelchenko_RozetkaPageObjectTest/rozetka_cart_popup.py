from selene import browser, by


class RozetkaCartPopup:

    def get_original_product_price(self, product_number):
        return browser.element(by.xpath("(//p[@class='cart-product__price'])[{0}]".format(str(product_number)))).text

    def get_discounted_product_price(self, product_number):
        return browser.element((by.xpath("(//p[@class='cart-product__price cart-product__price--red'])[{0}]"
                                         .format(str(product_number))))).text

    def get_product_name(self, product_number):
        return browser.element(by.xpath("(//div[@class='cart-product__main']/a)[{0}]"
                                        .format(str(product_number)))).text
