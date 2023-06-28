# 5 Task
from iherb_home_page import HomePage
from time import sleep

home_page = HomePage().open()

site_preference_popup = home_page.open_site_preference_popup()
home_page = site_preference_popup.change_country('US', '92571')
sleep(3)

search_results_page = home_page.search('vitamin k2')
search_results_page.verify_size_at_least(5)

search_results_page.set_filter('NOW Foods')
sleep(5)

number_of_product = 3
third_product_name = search_results_page.get_product_name(number_of_product)
third_product_price = search_results_page.get_product_price(number_of_product)
third_product = search_results_page.add_to_cart(number_of_product)

cart_page = third_product.open_cart_page()
product_name_cart = cart_page.get_product_name(1)
product_price_cart = cart_page.get_product_price(1)

assert third_product_name == product_name_cart, f'Product names are different'
assert third_product_price == product_price_cart, f'Product prices are different'

login_page = cart_page.open_login_page()
login_page.verify_opened().login_cart('1100test@yopmail.com', 'Qwertyui')
checkout_page = cart_page.open_checkout_page()
checkout_page.place_order()
