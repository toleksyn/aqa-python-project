from selene import browser, by, be, have

from iherbtestvenv.iherb_modal_container import IherbModalContainer
from iherbtestvenv.product_details_page import ProductDetailsPage

class IherbSearchPage:

    def verify_search_results_at_least(self, number_of_results):
        browser.all('//a/span[contains(text(), "")]').should(have.size_at_least(number_of_results))

    def get_product_review(self, product_number):
        return browser.element(by.xpath(format("//span[contains(text(),'6817')])[{0}]"
                                               .format(str(product_number)))))

    def open_product_details_page(self, product_number) -> ProductDetailsPage:
        browser.element(by.xpath(format('(//div[@class="product ga-product"])[{0}]'.format(str(product_number))))).click()
        return ProductDetailsPage()

    def verify_that_now_foods_checkbox_is_displayed_on_the_search_page(self):
        browser.element(by.xpath("//input[@id='FilterNOWFoodsNOW']")).should(be.visible and be.enabled)

    def get_all_displayed_products_with_now_foods_in_the_name(self, product_name):
        products = browser.all(by.xpath('//*[@id="FilteredProducts"]/div'))
        return [product_name for product in products if product_name and product_name.find != -1]

    def get_product_name(self, product_number):
        return browser.element(by.xpath(format("(//div[@class='product ga-product'])[{0}]"
                                               .format(str(product_number)))))

    def add_product_to_the_cart(self, product_name) -> IherbModalContainer:
        browser.element(by.xpath('form-add-to-cart add-to-cart-wrapper')).click()
        return IherbModalContainer()