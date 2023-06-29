from pages.iherb_home_page import IherbHomePage

def test_iherb_the_second_task():

    home_page = IherbHomePage().open()

    search_result_page = home_page.search("vitamin d")

    search_result_page.verify_search_results_at_least(5)

    search_result_page.set_the_filter("NOW Foods")

    products_include_filter_name = search_result_page.verify_that_products_include_filter_name("NOW Foods")

