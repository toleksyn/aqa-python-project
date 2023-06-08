from pages.rozetka_product_page import RozetkaProductPage


def test_rozetka_search_iphone(rozetka_home_page, rozetka_search_results_page, rozetka_product_page):
    rozetka_home_page.open()
    rozetka_home_page.search("iPhone")

    rozetka_search_results_page.verify_search_results_at_least(5)

    # price from search
    search_price = rozetka_search_results_page.get_product_price_from_search_result(3)

    rozetka_search_results_page.open_product_page(3)

    # price_from_pdp
    price_from_product_page = rozetka_product_page.get_price_from_pdp()

    assert search_price == price_from_product_page
