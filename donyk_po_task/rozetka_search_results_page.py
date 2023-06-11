from selene import browser, by, have


class SearchResultsPage:

    def verify_size_at_least(self, number_of_results):
        browser.all(by.xpath('//a/span[contains(text(),"")]')).should(have.size_at_least(number_of_results))

    def get_product_price(self, product_number):
        return browser.element(by.xpath(format('(//span[@class="goods-tile__price-value"])[{0}]'.format(str(product_number))))).text

    def open_product_page(self, product_number):
        browser.element(by.xpath('(//span[@class="goods-tile__title"])[{0}]'.format(str(product_number)))).click()
        from rozetka_product_page import ProductPage
        return ProductPage()

    def get_product_name(self, product_number):
        return browser.element(by.xpath(format('(//span[@class="goods-tile__title"])[{0}]'.format(str(product_number))))).text

    def add_product_to_cart(self, product_number):
        browser.element(by.xpath('(//button[@class="buy-button goods-tile__buy-button ng-star-inserted"])[{0}]'.format(str(product_number)))).click()
        return self

    def open_cart_popup(self):
        browser.element(by.xpath('//button[@class="header__button ng-star-inserted header__button--active"]')).click()
        from rozetka_cart_popup import CartPopup
        return CartPopup()
