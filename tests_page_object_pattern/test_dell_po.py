from selene import browser, by, be, have, config

from rozetka_home_page import RozetkaHomePage
<<<<<<< HEAD
=======
from rozetka_search_results_page import RozetkaSearchResultsPage
from product_details_page import ProductDetailsPage
from basket_modal import BasketModal
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71

def test_rozetka_search_po():
    config.timeout = 40

<<<<<<< HEAD
    home_page = RozetkaHomePage().open()
    search_results = home_page.search("dell")
    search_results.verify_search_results_at_least(10)
    fifth_product_name_on_search_page = search_results.get_product_name(5)
    fifth_product_price_on_search_page = search_results.get_product_price(5)
    add_fifth_product_to_basket = search_results.add_product_to_basket(5)
    basket_modal = search_results.open_basket_modal()
    product_name_in_basket = basket_modal.get_product_name(1)
    product_price_in_basket = basket_modal.get_discounted_product_price(1)
    assert fifth_product_name_on_search_page == product_name_in_basket, f'Product`s name in Basket is incorrect'
    assert fifth_product_price_on_search_page == product_price_in_basket, f'Product`s price in Basket is incorrect'
=======
    home_page = RozetkaHomePage()
    home_page.open()

    results_page = home_page.search("Dell")

    results_page.verify_search_results_at_least(10)

    pdp_results_page = ProductDetailsPage()
    product_name_on_search_page = pdp_results_page.verify_product_name_present(product_number=5)
    product_price_on_search_page = pdp_results_page.verify_product_price_present_on_pdp(product_number=5)

    add_product_to_basket = RozetkaSearchResultsPage().add_products_to_basket(product_number=5)

    basket_modal = BasketModal()
    basket_modal.verify_that_basket_modal_is_open()
    product_name_in_basket = basket_modal.verify_product_name_in_basket()
    product_price_in_basket = basket_modal.verify_product_price_in_basket()

    assert product_name_on_search_page == product_name_in_basket, f'Product`s name in Basket is incorrect'
    assert product_price_on_search_page == product_price_in_basket, f'Product`s price in Basket is incorrect'
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71
