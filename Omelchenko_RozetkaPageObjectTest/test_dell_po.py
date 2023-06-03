# - Open http://rozetka.com.ua home page
# - Search for ‘dell’
# - Verify that at least 10 result links are displayed
# - Save the name and the price of 5th product, add it to the basket
# - Verify the basket modal is opened and the price and name are correct
from Omelchenko_RozetkaPageObjectTest.rozetka_home_page import RozetkaHomePage

# Task 1
home_page = RozetkaHomePage().open()

search_results = home_page.search('dell')
search_results.verify_search_results_have_size_at_least(10)

fifth_product_price = search_results.get_product_price(5)
fifth_product_name = search_results.get_product_name(5)
add_fifth_product_to_cart = search_results.add_to_cart(5)

cart_popup = search_results.open_cart_popup()
product_name_in_cart = cart_popup.get_product_name(1)
product_price_in_cart = cart_popup.get_discounted_product_price(1)

assert fifth_product_name == product_name_in_cart, f'Product names are not equal'
assert fifth_product_price == product_price_in_cart, f'Product prices are not equal'
