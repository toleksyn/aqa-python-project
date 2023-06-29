from pages.iherb_home_page import IherbHomePage


def test_iherb_the_first_task():

    home_page = IherbHomePage().open()

    search_result_page = home_page.search("vitamin a")

    search_result_page.verify_search_results_at_least(5)

    review_count_from_search_results = search_result_page.get_reviews_count_from_search_results(5)

    product_page = search_result_page.open_the_product_details_page(5)

    review_count_from_product_page = product_page.get_reviews_count_from_product_page()

    assert review_count_from_search_results == review_count_from_product_page, f'Reviews counts are not equal'
