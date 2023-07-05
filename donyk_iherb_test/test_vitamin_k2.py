# 5 Task
from selene import browser
from iherb_home_page import HomePage

browser.config.timeout = 30

home_page = HomePage().open()

site_preference_popup = home_page.open_site_preference_popup()
home_page = site_preference_popup.change_country('US')

search_results_page = home_page.search('vitamin k2')
search_results_page.verify_search_results_at_least(5)

filter_name = 'NOW Foods'
search_results_page.set_filter(filter_name)

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
login_page.verify_opened().log_in_on_cart('1100test@yopmail.com', 'Qwertyui')
checkout_page = cart_page.open_checkout_page()

update_payment_page = checkout_page.place_order()
orders_page = update_payment_page.open_orders_page()
orders_page.verify_order_number_is_displayed()
