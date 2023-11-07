from selene import browser

from iherbtestvenv.iherb_home_page import IherbHomePage

def test_search_vitamin_a():
    browser.config.timeout = 40

    home_page = IherbHomePage().open()

    site_preference_modal = home_page.open_site_preference_modal()
    site_preference_modal.select_language('English')

    search_results_page = home_page.search('vitamin a')
    search_results_page.verify_search_results_at_least(5)

    product_number = 5
    fifth_product_review_on_search_page = search_results_page.get_product_reviews_count(product_number)
    fifth_product_details_page = search_results_page.open_product_details_page(product_number)
    fifth_product_review_on_details_page = fifth_product_details_page.get_product_reviews_amount()

    assert fifth_product_review_on_search_page == fifth_product_review_on_details_page, f"The stored review and review on " \
                                                                                    f"product page is not equal"
