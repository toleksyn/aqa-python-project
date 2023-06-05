from selene import browser, by, be, have

class RozetkaBasketModal:

<<<<<<< HEAD
    def get_original_product_price(self, product_number):
        return browser.element(by.xpath(format("(//p[@class='cart-product__price'])[{0}]".format(str(product_number))))).text

    def get_discounted_product_price(self, product_number):
        return browser.element(by.xpath(format("(//p[@class='cart-product__price cart-product__price--red'])[{0}]"
                                         .format(str(product_number))))).text

    def get_product_name(self, product_number):
        return browser.element(by.xpath(format("(//div[@class='cart-product__main']/a)[{0}]"
                                        .format(str(product_number))))).text
=======
    def verify_that_basket_modal_is_open(self):
        browser.element(by.xpath("//rz-cart/button")).click()

    def verify_product_name_in_basket(self):
        browser.element(by.xpath('//div[@class="cart-product__main"]/a')).should(be.existing).text

    def verify_product_price_in_basket(self):
        browser.element(by.xpath('//p[@class="cart-product__price"]')).should(be.existing).text

    def verify_order_button(self):
        browser.element(by.xpath('//a[@data-testid="cart-receipt-submit-order"]')).should(be.existing)

        return BasketModal
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71
