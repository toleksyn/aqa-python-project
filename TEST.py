from selene import browser, by, have, query, be

class HomePage:
    def open(self):
        browser.open("https://rozetka.com.ua/")

    def search(self, keyword):
        browser.element(by.name("search")).type(keyword).press_enter()
        return SearchResults()

class SearchResults:
    def verify_search_results_at_least(self, number_of_results):
        browser.all(by.xpath("//a[contains(@class, 'goods-tile__heading')]")).should(have.size_greater_than_or_equal(number_of_results))

    def get_product_price_from_search_result(self, number_of_results):
        all_products = browser.all(by.xpath('//span[@class="goods-tile__price-value"]'))
        product_item = all_products[number_of_results - 1]
        return product_item.get(query.text)

    def get_product_name_from_search_result(self, number_of_results):
        all_products = browser.all(by.xpath('//a[contains(@class, "goods-tile__heading")]/span'))
        product_item = all_products[number_of_results - 1]
        return product_item.get(query.text)

    def add_product_to_cart(self, number_of_results):
        add_to_cart_buttons = browser.all(by.xpath('//button[@class="buy-button goods-tile__buy-button ng-star-inserted"]'))
        add_to_cart_button = add_to_cart_buttons[number_of_results - 1]
        add_to_cart_button.click()

    def open_cart_modal(self):
        cart_icon = browser.element(by.xpath('//rz-cart'))
        cart_icon.click()


class CartModal:
    def verify_cart_modal_is_open(self):
        modal_header = browser.element(by.xpath('//div[@class="modal__header"]'))
        place_order_button = browser.element(by.xpath('//a[@class="button button_size_large button_color_green cart-receipt__submit ng-star-inserted"]'))

        modal_header.should(be.visible)
        place_order_button.should(be.visible)

    def get_product_name_from_cart(self):
        product_name_element = browser.element(by.xpath('//a[@class="cart-product__title"]'))
        return product_name_element.get(query.text)

    def get_product_price_from_cart(self):
        product_price_element = browser.element(by.xpath('//p[@class="cart-product__price cart-product__price--red"]'))
        return product_price_element.get(query.text)


def test_rozetka_search_and_add_to_cart():
    # Create page objects
    home_page = HomePage()
    search_results_page = SearchResults()
    cart_modal = CartModal()

    # Open home page
    home_page.open()

    # Search for 'dell'
    home_page.search("dell")

    # Verify search results
    search_results_page.verify_search_results_at_least(10)

    # Get product name and price from search result
    search_product_name = search_results_page.get_product_name_from_search_result(5)
    search_product_price = search_results_page.get_product_price_from_search_result(5)

    # Add product to cart
    search_results_page.add_product_to_cart(5)

    # Open cart modal
    search_results_page.open_cart_modal()

    # Verify cart modal is open
    cart_modal.verify_cart_modal_is_open()

    # Get product name and price from cart
    cart_product_name = cart_modal.get_product_name_from_cart()
    cart_product_price = cart_modal.get_product_price_from_cart()

    # Verify the name and price
    assert search_product_name == cart_product_name
    assert search_product_price == cart_product_price


# Run the test
test_rozetka_search_and_add_to_cart()
