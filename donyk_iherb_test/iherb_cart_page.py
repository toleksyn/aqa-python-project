from selene import browser, by, be


class CartPage:

    def verify_product_added_to_cart(self):
        browser.element(by.xpath('//div[@id="mainCartContainer"]')).should(be.visible)

    def open_checkout_page(self):
        browser.element(by.xpath('//div[@class="css-1ijv08"]/a')).click()
        from iherb_checkout_page import CheckoutPage
        return CheckoutPage()
