from selene import browser, by, be, have

from iherbtestvenv.iherb_modal_overlay import IherbModalOverlay
from iherbtestvenv.iherb_product_details_page import IherbProductDetailsPage

class IherbSearchResultsPage:

    def verify_search_results_at_least(self, number_of_results):
        browser.all('//a/span[contains(text(), "")]').should(have.size_at_least(number_of_results))

    def get_product_reviews_count(self, product_number):
        return browser.element(by.xpath("(//a[@class='rating-count'])[{0}]/span".format(str(product_number)))).text

    def open_product_details_page(self, product_number) -> IherbProductDetailsPage:
        browser.element(by.xpath("(//a[@class='absolute-link product-link'])[{0}]".format(str(product_number)))).click()
        return IherbProductDetailsPage()

    def set_brands_filter(self, filter_value):
        browser.element(by.xpath('//div[@class="filter-name"]'.format(filter_value))).wait_until(be.visible)
        browser.element(by.xpath('//div[@class="filter-name"]'.format(filter_value))).click()
        return self

    def verify_that_all_products_are_filtered_by(self, filter_value):
        browser.element(by.xpath("//div[@class='product-inner product-inner-wide']/div/div/bdi[contains(text(), '{}')]"
                                 .format(str(filter_value))))

    def get_product_name(self, product_number):
        return browser.element(by.xpath("(//div[@class='product-inner product-inner-wide']/div/div/bdi)[{0}]"
                                        .format(str(product_number)))).text

    def add_product_to_cart(self, product_number) -> IherbModalOverlay:
        browser.element(by.xpath('//button[@class="btn btn-primary btn-add-to-cart gtm-add-to-cart"][{0}]'.\
                                 format(str(product_number)))).click()
        return IherbModalOverlay()