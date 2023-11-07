from selene import browser, by, be, have, query

from iherbtestvenv.iherb_modal_overlay import IherbModalOverlay
from iherbtestvenv.iherb_product_details_page import IherbProductDetailsPage

class IherbSearchResultsPage:

    def verify_search_results_at_least(self, number_of_results):
        browser.all(by.xpath("//a[@class='absolute-link product-link']"))\
            .should(have.size_at_least(number_of_results))

    def get_product_reviews_count(self, product_number):
        return browser.element(by.xpath("(//a[@class='rating-count'])[{0}]/span".format(str(product_number)))).get(query.text)

    def open_product_details_page(self, product_number) -> IherbProductDetailsPage:
        browser.element(by.xpath("(//a[@class='absolute-link product-link'])[{0}]".format(str(product_number)))).click()
        return IherbProductDetailsPage()

    def set_brands_filter(self, filter_value):
        browser.element(by.xpath("//li[@data-keyword='{}']".format(filter_value))).click()
        browser.element(by.xpath("//div[@class='applied-filters']")).wait.until(be.visible)
        return self

    def verify_that_all_products_are_filtered_by(self, filter_value):
        browser.element(by.xpath("//div[@class='product-inner product-inner-wide']/div/div/bdi[contains(text(), '{}')]"
                                 .format(str(filter_value))))

    def get_product_name(self, product_number):
        return browser.element(by.xpath("(//div[@class='product-inner product-inner-wide']/div/div/bdi)[{0}]"
                                        .format(str(product_number)))).get(query.text)

    def add_product_to_cart(self, product_number) -> IherbModalOverlay:
        product_card = browser.element(by.xpath("(//div[@class='product ga-product'])[{0}]"
                                                .format(str(product_number))))
        product_card.hover().element(by.xpath("(//button[@name='AddToCart'])[{0}]"
                                              .format(str(product_number)))).click()
        return IherbModalOverlay()

    def get_original_product_price(self, product_number):
        return browser.element(by.xpath("(//span[@class='price ']/bdi)[{0}]"
                                        .format(str(product_number)))).get(query.text)

    def get_discounted_product_price(self, product_number):
        return browser.element(by.xpath("(//span[@class='price discount-red']/bdi)[{0}]"
                                        .format(str(product_number)))).get(query.text)