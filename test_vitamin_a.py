from selene import browser, by, be, have, config

from iherbtestvenv.iherb_home_page import IherbHomePage

def test_iherb_search_po():
    config.timeout = 40

    home_page = IherbHomePage().open()
    results_page = home_page.search('vitamin a')
    results_page.verify_search_results_at_least(5)
    fifth_product_review_on_search_page = results_page.get_product_review(5)
    fifth_product_details_page = results_page.open_product_details_page(5)
    product_review_on_details_page = fifth_product_details_page.get_product_review_on_details_page()
    assert fifth_product_review_on_search_page == fifth_product_review_on_search_page, f"The stored review and review on " \
                                                                                       f"product page is not equal"