from pages.iherb_home_page import IherbHomePage
from pages.iherb_search_results_page import IherbSearchResultsPage

def test_iherb_the_second_task():
    # Open iherb home page
    home_page = IherbHomePage()
    home_page.open()

    # Search for ‘vitamin d’
    home_page.search("vitamin d")

    # Verify at least 5 products are displayed
    search_result_page = IherbSearchResultsPage()
    search_result_page.verify_search_results_at_least(5)

    # In the filter section, check the NOW Foods checkbox
    search_result_page.set_the_filter("NOW Foods")

    # Verify that all displayed products title have ‘NOW Foods’ in the name
    filter_name = "NOW Foods"
    product_titles_include_filter_name = search_result_page.get_filter_name_from_all_product_titles()

    assert filter_name == product_titles_include_filter_name, f'The product titles do not include the "NOW Foods" filter name'
