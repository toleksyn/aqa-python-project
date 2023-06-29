from selene import browser, by, have, query, be

from pages.iherb_cart_modal import IherbCartModal
from pages.iherb_product_details_page import IherbProductDetailsPage

class IherbSearchResultsPage:
    def verify_search_results_at_least(self, number_of_search_results):
        browser.all(by.xpath("//a[@class='absolute-link product-link']")).should(have.size_greater_than_or_equal(number_of_search_results))

    def get_reviews_count_from_search_results(self, number_of_search_results):
        return browser.element(by.xpath(f"(//a[@class='rating-count'])[{number_of_search_results}]")).get(query.text)

    def open_the_product_details_page(self, product_number) -> IherbProductDetailsPage:
        browser.element(by.xpath(f"//a[@data-ga-product-position='{product_number}']")).click()
        return IherbProductDetailsPage()

    def set_the_filter(self, filter_name):
        browser.element(by.xpath(f'//label[contains(text(),"{filter_name}")]')).click()
        return IherbSearchResultsPage

    def verify_that_products_include_filter_name(self, filter_name_from_product):
        products_include_filter_name = browser.all(by.xpath(f'(//a[contains(@title, "{filter_name_from_product}")])'))
        for element in products_include_filter_name:
            element.should(be.visible)

    def get_product_name(self, product_number):
        browser.element(by.xpath(f'(//div[@class="product-inner product-inner-wide"]/div/div/bdi)[{product_number}]')).get(query.inner_html)
        return IherbSearchResultsPage()

    def hover_to_the_add_cart_button(self, product_number):
        xpath = f'(//button[@name="AddToCart"])[{product_number}]'
        browser.element(by.xpath(xpath)).hover()
        return self

    def add_product_to_the_cart(self, product_number):
        xpath = f'(//button[@name="AddToCart"])[{product_number}]'
        browser.element(by.xpath(xpath)).click()
        return IherbCartModal()
