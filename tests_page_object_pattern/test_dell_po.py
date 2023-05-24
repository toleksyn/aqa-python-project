from selene import browser, by, be, have
from selene import config
import pytest

from rozetka_home_page import RozetkaHomePage
from rozetka_search_results_page import RozetkaSearchResultsPage
from products_open import ProductsOpen
from basket_modal import BasketModal

def test_rozetka_search_po():
    config.timeout = 40
# Open http://rozetka.com.ua home page
    home_page = RozetkaHomePage()
    home_page.open()
# Search for ‘dell’
    results_page = home_page.search("Dell")
# Verify that at least 10 result links are displayed
    results_page.verify_search_results_at_least(10)
# Save the name and the price of 5th product, add it to the basket
    pdp_results_page = ProductsOpen()
    product_name_plp = pdp_results_page.verify_product_name_present(product_number=5)
    product_price_plp = pdp_results_page.verify_product_price_present_on_pdp(product_number=5)
    add_product_to_basket = RozetkaSearchResultsPage()
    add_product_to_basket.add_products_to_basket(product_number=5)
 # Verify the basket modal is opened and the price and name are correct
    basket_modal = BasketModal()
    basket_modal.verify_basket_modal_title()
    basket_modal.verify_close_modal_button()
    product_name_basket = basket_modal.verify_product_name_in_basket()
    product_price_basket = basket_modal.verify_product_price_in_basket()
    basket_modal.verify_order_button()
    assert product_name_plp == product_name_basket, f'Product`s name in Basket is incorrect'
    assert product_price_plp == product_price_basket, f'Product`s price in Basket is incorrect'
