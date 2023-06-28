from selene import browser, by, have


class SearchResultsPage:

    def verify_size_at_least(self, number_of_results):
        browser.all(by.xpath('//a[@class="absolute-link product-link"]')).should(have.size_at_least(number_of_results))

    def get_product_reviews_count(self, product_number):
        return browser.element(by.xpath(format('(//a[@class="rating-count"])[{0}]/span'.format(str(product_number))))).text

    def open_product_page(self, product_number):
        browser.element(by.xpath('(//a[@class="absolute-link product-link"])[{0}]'.format(str(product_number)))).click()
        from iherb_product_page import ProductPage
        return ProductPage()

    def set_filter(self, filter):
        browser.element(by.xpath('//li[@data-keyword="{}"]'.format(filter))).click()
        return self

    def get_product_name(self, product_number):
        return browser.element(by.xpath('(//div[@class="product-title"])[{0}]'.format(str(product_number)))).text

    def add_to_cart(self, product_number):
        browser.element(by.xpath('(//button[@name="AddToCart"])[{0}]'.format(str(product_number)))).click()
        from iherb_cart_popup import CartPopup
        return CartPopup()

    def change_to_list_view(self):
        browser.element(by.xpath('//*[name()="svg"][@class="icon icon-list-view toggle-view-type selected"]')).click()
        return self

    def get_product_price(self, product_number):
        return browser.element(by.xpath('(//div[@class="product-price-top"])[{0}]'.format(str(product_number)))).text
