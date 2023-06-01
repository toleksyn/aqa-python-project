from selene import config
from rozetka_home_page import RozetkaHomePage
from rozetka_product_page import RozetkaProductPage
from rozetka_search_results_page import RozetkaSearchResultsPage


def test_rozetka():
    config.timeout = 40

    rozetka_home_page = RozetkaHomePage()
    rozetka_search_results_page = RozetkaSearchResultsPage()
    rozetka_product_page = RozetkaProductPage()

    rozetka_home_page.open()
    rozetka_home_page.search('iPhone')

    rozetka_search_results_page.verify_search_results_at_least(5)

    # price from search
    search_price = rozetka_search_results_page.get_price_from_search_result(3)
    print("Search Price:", search_price)

    rozetka_search_results_page.open_product_number_three(3)

    # price_from_pdp
    pdp_price = rozetka_product_page.get_price_from_pdp()
    print("PDP Price:", pdp_price)

    assert search_price == pdp_price
    #ssert search_price == pdp_price
           #^^^^^^^^^^^^^^^^^^^^^^^^^
#AssertionError


test_rozetka()
