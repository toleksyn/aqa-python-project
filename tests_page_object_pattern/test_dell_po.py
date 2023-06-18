from selene import browser, by, be, have
from selene import config

from rozetka_home_page import RozetkaHomePage

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
