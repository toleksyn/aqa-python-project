from selene import browser, by, be, have
from selene import config
import pytest

from rozetka_home_page import RozetkaHomePage
from products_open import ProductsOpen

def test_rozetka_search_po():
    config.timeout = 40
# Open http://rozetka.com.ua home page
    home_page = RozetkaHomePage()
    home_page.open()
# Search for ‘iPhone’
    results_page = home_page.search("iPhone")
    # Verify that at least 5 result links are displayed and that each link text contains 'iPhone'
    results_page.verify_search_results_at_least(5)
# Verify the 3rd product has a price, save the price
    price_plp = results_page.verify_product_price_present(product_number=3)
# Click on the 3rd product and verify that the stored price and price on product page is equal
    pdp_results_page = ProductsOpen()
    price_pdp = pdp_results_page.verify_product_price_present_on_pdp(product_number=3)
    assert price_plp == price_pdp, f'The stored price and price on product page is not equal'
