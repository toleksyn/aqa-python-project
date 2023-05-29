from selene import browser, by


class RozetkaCartPopup:

    def get_product_price(self):
        return browser.element(by.xpath("//p[@class='cart-product__price']")).text

    def get_product_name(self):
        return browser.element(by.xpath("//div[@class='cart-product__main']/a")).text
