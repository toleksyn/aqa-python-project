from pages.iherb_home_page import IherbHomePage
from pages.iherb_search_results_page import IherbSearchResultsPage
from pages.iherb_product_details_page import IherbProductDetailsPage


def test_iherb_the_first_task():
    # Open iherb home page
    home_page = IherbHomePage()
    home_page.open()

    # Search for ‘vitamin a’
    home_page.search("vitamin a")

    # Verify at least 5 products are displayed
    search_result_page = IherbSearchResultsPage()
    search_result_page.verify_search_results_at_least(5)

    # Get the reviews count for 5th product from search result
    review_count_from_search_results = search_result_page.get_reviews_count_from_search_results(5)

    # Open the product details page
    search_result_page.open_the_product_details_page(5)

    # Get the reviews count for product from product details page
    product_page = IherbProductDetailsPage()
    review_count_from_product_page = product_page.get_reviews_count_from_product_page()

    assert review_count_from_search_results == review_count_from_product_page, f'Reviews counts are not equal'

