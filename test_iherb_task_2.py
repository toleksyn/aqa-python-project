from pages.iherb_home_page import IherbHomePage

def test_iherb_the_second_task():
    # Open iherb home page
    home_page = IherbHomePage().open()

    # Search for ‘vitamin d’
    search_result_page = home_page.search("vitamin d")

    # Verify at least 5 products are displayed
    search_result_page.verify_search_results_at_least(5)

    # In the filter section, check the NOW Foods checkbox
    search_result_page.set_the_filter("NOW Foods")

    # Verify that all displayed products have ‘NOW Foods’ in the name
    products_include_filter_name = search_result_page.verify_that_products_include_filter_name("NOW Foods")

