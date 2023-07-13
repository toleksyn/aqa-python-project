from selene import browser, by, be, query


class CartPage:

    def open_checkout_page(self):
        browser.element(by.xpath('//div[@class="css-1ijv08"]/a')).click()
        from iherb_checkout_page import CheckoutPage
        return CheckoutPage()

    def get_product_name(self, product_number):
        return browser.element(by.xpath('(//a[@class="css-1wm8slt"])[{0}]'.format(str(product_number)))).get(query.text)

    def get_product_price(self, product_number):
        return browser.element(by.xpath('(//div[@class="css-1wxlbl4"])[{0}]'.format(str(product_number)))).get(query.text)

    def open_login_page(self):
        browser.element(by.xpath('//div[@id="iherb-account"]/div/span/a')).click()
        from iherb_login_page import LoginPage
        return LoginPage()
