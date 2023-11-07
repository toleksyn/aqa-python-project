from selene import browser

from iherbtestvenv.iherb_home_page import IherbHomePage

def test_search_vitamin_d():
    browser.config.timeout = 40

    home_page = IherbHomePage().open()

    site_preference_modal = home_page.open_site_preference_modal()
    home_page = site_preference_modal.select_language('English')

    search_results_page = home_page.search('vitamin d')
    search_results_page.verify_search_results_at_least(5)

    filter_name = 'NOW Foods'
    search_results_page.set_brands_filter(filter_name)

    first_product_name = search_results_page.get_product_name(1)
    last_product_name = search_results_page.get_product_name(48)
    middle_product_name = search_results_page.get_product_name(24)

    assert first_product_name.startswith(filter_name), f"The product has no 'Now Foods' name"
    assert last_product_name.startswith(filter_name), f"The product has no 'Now Foods' name"
    assert middle_product_name.startswith(filter_name), f"The product has no 'Now Foods' name"
