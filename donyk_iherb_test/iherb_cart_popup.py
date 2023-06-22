from selene import browser, by, be


class CartPopup:

    def verify_product_added_to_cart(self):
        browser.element(by.xpath('//div[@class="add-to-cart-product"]')).should(be.visible)

    def open_cart_page(self):
        browser.element(by.xpath('//div[@class="checkout-button"]')).click()
        from iherb_cart_page import CartPage
        return CartPage()
