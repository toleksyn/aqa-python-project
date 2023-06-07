from selene import browser, by, be, query


class RozetkaCartModal:
    def verify_cart_modal_is_open(self):
        modal_header = browser.element(by.xpath('//div[@class="modal__header"]'))
        place_order_button = browser.element(by.xpath('//a[@class="button button_size_large button_color_green cart-receipt__submit ng-star-inserted"]'))

        modal_header.should(be.visible)
        place_order_button.should(be.visible)

    def get_product_name_from_cart(self, number_of_results):
        product_name_elements = browser.all(by.xpath('//a[@class="cart-product__title"]'))
        product_name_element = product_name_elements[number_of_results - 1]
        return product_name_element.get(query.text)

    def get_product_price_from_cart(self):
        product_price_element = browser.element(by.xpath('//p[@class="cart-product__price cart-product__price--red"]'))
        return product_price_element.get(query.text)

