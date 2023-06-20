from selene import browser, by, have, query
from pages.iherb_product_details_page import IherbProductDetailsPage


class IherbSearchResultsPage:
    def verify_search_results_at_least(self, number_of_search_results):
        browser.all(by.xpath("//a[@class='absolute-link product-link']")).should(have.size_greater_than_or_equal(number_of_search_results))

    def get_reviews_count_from_search_results(self, number_of_search_results):
        return browser.element(by.xpath(f"(//a[@class='rating-count'])[{number_of_search_results}]")).get(query.text)

    def open_the_product_details_page(self, number_of_search_results) -> IherbProductDetailsPage:
        browser.element(by.xpath(f"//a[@data-ga-product-position='{number_of_search_results}']")).click()
        return IherbProductDetailsPage()

    def click_the_filter_checkbox(self, filter_name):
        browser.element(by.xpath(f'//label[contains(text(),"{filter_name}")]')).click()
        return self

    def get_filter_name_from_all_product_titles(self):
        browser.all(by.xpath(f'(//a[contains(@title, "NOW Foods")])')).get(query.text)
        return self
