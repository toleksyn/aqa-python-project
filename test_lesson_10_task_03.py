from selene import browser, by, have, query

from pages.rozetka_home_page import RozetkaHomePage
from pages.rozetka_search_results_page import RozetkaSearchResultsPage
from pages.rozetka_cart_modal import RozetkaCartModal


def test_rozetka_add_to_cart():
    home_page = RozetkaHomePage()
    home_page.open()

    search_results_page = RozetkaSearchResultsPage()
    home_page.search("dell")
    search_results_page.verify_search_results_at_least(10)

    cart_modal = RozetkaCartModal()

    # Get product name and price from search result
    search_product_name = search_results_page.get_product_name_from_search_result(5)
    search_product_price = search_results_page.get_product_price_from_search_result(5)

    search_results_page.add_product_to_the_cart(5)

    search_results_page.open_the_cart_modal()
    cart_modal.verify_cart_modal_is_open()

    # Get product name and price from cart
    cart_product_name = cart_modal.get_product_name_from_cart(0)
    cart_product_price = cart_modal.get_product_price_from_cart()

    assert search_product_price == cart_product_price
    assert search_product_name == cart_product_name



test_rozetka_add_to_cart()
