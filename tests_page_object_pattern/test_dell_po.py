from selene import browser, by, be, have
from selene import config
import pytest

from rozetka_home_page import RozetkaHomePage
from rozetka_search_results_page import RozetkaSearchResultsPage
from product_details_page import ProductDetailsPage
from basket_modal import BasketModal

def test_rozetka_search_po():
    config.timeout = 40

    home_page = RozetkaHomePage()
    home_page.open()

    results_page = home_page.search("Dell")

    results_page.verify_search_results_at_least(10)

    pdp_results_page = ProductDetailsPage()
    product_name_on_search_page = pdp_results_page.verify_product_name_present(5)
    product_price_on_search_page = pdp_results_page.verify_product_price_present_on_pdp(5)

    add_product_to_basket = RozetkaSearchResultsPage().add_products_to_basket(5)

    basket_modal = BasketModal()
    basket_modal.verify_that_basket_modal_is_open()
    product_name_in_basket = basket_modal.verify_product_name_in_basket()
    product_price_in_basket = basket_modal.verify_product_price_in_basket()

    assert product_name_on_search_page == product_name_in_basket, f'Product`s name in Basket is incorrect'
    assert product_price_on_search_page == product_price_in_basket, f'Product`s price in Basket is incorrect'
