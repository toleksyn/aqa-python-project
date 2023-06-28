from selene import browser, by, be


class CartPage:

    def verify_product_added_to_cart(self):
        browser.element(by.xpath('//div[@id="mainCartContainer"]')).should(be.visible)

    def open_checkout_page(self):
        browser.element(by.xpath('//div[@class="css-1ijv08"]/a')).click()
        from iherb_checkout_page import CheckoutPage
        return CheckoutPage()

    def get_product_name(self, product_number):
        return browser.element(by.xpath('(//a[@class="css-1wm8slt"])[{0}]'.format(str(product_number)))).text

    def get_product_price(self, product_number):
        return browser.element(by.xpath('(//div[@class="css-1wxlbl4"])[{0}]'.format(str(product_number)))).text
