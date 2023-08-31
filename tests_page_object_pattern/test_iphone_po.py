from selene import browser, by, be, have, config

from rozetka_home_page import RozetkaHomePage

home_page = RozetkaHomePage().open()
search_results_page = home_page.search("iPhone")
search_results_page.verify_search_results_at_least(5)

product_number = 3
third_product_price_on_search_page = search_results_page.get_product_price(product_number)
third_product_details_page = search_results_page.open_product(product_number)
price_on_product_details_page = third_product_details_page.get_discounted_product_price()
assert third_product_price_on_search_page == price_on_product_details_page, f'The stored price and price on product page is not equal'
