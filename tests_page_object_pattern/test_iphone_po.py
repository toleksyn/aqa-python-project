from selene import browser, by, be, have, config

from rozetka_home_page import RozetkaHomePage
<<<<<<< HEAD
=======
from product_details_page import ProductDetailsPage
from rozetka_search_results_page import RozetkaSearchResultsPage
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71

def test_rozetka_search_po():
    config.timeout = 40

<<<<<<< HEAD
    home_page = RozetkaHomePage().open()
    search_results = home_page.search("iPhone")
    search_results.verify_search_results_at_least(5)
    third_product_price_on_search_page = search_results.get_product_price(3)
    third_product_details_page = search_results.open_product_details_page(3)
    price_on_product_details_page = third_product_details_page.get_discounted_product_price()
    assert third_product_price_on_search_page == price_on_product_details_page, f'The stored price and price on product page is not equal'
=======
    home_page = RozetkaHomePage()
    home_page.open()

    search_results_page = home_page.search("iPhone")

    search_results_page.verify_search_results_at_least(5)

    product_price_on_search_page = search_results_page.verify_product_price_present(product_number=3)

    product_open = RozetkaSearchResultsPage().open_the_product(product_number=3)

    product_results_page = ProductDetailsPage()
    price_on_product_page = product_results_page.verify_product_price_present_on_pdp(product_number=3)

    assert product_price_on_search_page == price_on_product_page, f'The stored price and price on product page is not equal'
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71