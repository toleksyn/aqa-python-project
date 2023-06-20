from selene import browser, by, have

from Omelchenko_iHerbTest.iherb_cart_modal import IherbCartModal
from Omelchenko_iHerbTest.iherb_product_details_page import IherbProductDetailsPage


class IHerbSearchResultsPage:

    def verify_that_search_results_have_size_at_least(self, results_number):
        browser.all(by.xpath("//a[@class='absolute-link product-link']"))\
            .should(have.size_at_least(results_number))

    def get_product_reviews_amount(self, product_number):
        return browser.element(by.xpath("(//a[@class='rating-count'])[{0}]/span".format(str(product_number)))).text

    def open_product_details_page(self, product_number) -> IherbProductDetailsPage:
        browser.element(by.xpath("(//a[@class='absolute-link product-link'])[{0}]".format(str(product_number)))).click()
        return IherbProductDetailsPage()

    def set_brands_filter(self, filter_value):
        browser.element(by.xpath("//li[@data-keyword='{}']".format(filter_value))).click()
        return self

    def verify_that_all_products_are_filtered_by(self, filter_value):
        browser.element(by.xpath("//div[@class='product-inner product-inner-wide']/div/div/bdi[contains(text(), '{}')]"
                                 .format(str(filter_value))))

    def get_product_name(self, product_number):
        return browser.element(by.xpath("(//div[@class='product-inner product-inner-wide']/div/div/bdi)[{0}]"
                                        .format(str(product_number)))).text

    def add_to_cart(self, product_number) -> IherbCartModal:
        browser.element(by.xpath("(//button[@name='AddToCart'])[{0}]".format(str(product_number)))).click()
        return IherbCartModal()

    def change_to_list_view(self):
        browser.element(by.xpath('//*[name()="svg" and @data-ga-event-label="Click-list view"]')).click()
        return self
