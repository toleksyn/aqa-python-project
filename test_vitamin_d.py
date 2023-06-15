from selene import browser, by, be, have, config

from iherbtestvenv.iherb_home_page import IherbHomePage

def test_iherb_search_po():
    config.timeout = 40

    home_page = IherbHomePage().open()
    results_page = home_page.search('vitamin d')
    results_page.verify_search_results_at_least(5)

    now_foods_checkbox = results_page.verify_that_now_foods_checkbox_is_displayed_on_the_search_page()
    now_foods_in_the_name = results_page.get_all_displayed_products_with_now_foods_in_the_name(product_name="NOW Foods")

    assert now_foods_in_the_name, "Not all displayed products have 'Now Foods' in the name"