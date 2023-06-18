from selene import browser, by, be, have, config

from rozetka_home_page import RozetkaHomePage

home_page = RozetkaHomePage().open()
search_results = home_page.search("iPhone")
search_results.verify_search_results_at_least(5)
third_product_price_on_search_page = search_results.get_product_price(3)
third_product_details_page = search_results.open_product_details_page(3)
price_on_product_details_page = third_product_details_page.get_discounted_product_price()
assert third_product_price_on_search_page == price_on_product_details_page, f'The stored price and price on product page is not equal'
