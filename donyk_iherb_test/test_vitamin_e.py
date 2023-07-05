# Task 4
from selene import browser
from iherb_home_page import HomePage

browser.config.timeout = 20

home_page = HomePage().open()

site_preference_popup = home_page.open_site_preference_popup()
home_page = site_preference_popup.change_country('US')

home_page.open_login_page().log_in('1100test@yopmail.com', 'Qwertyui')

search_results_page = home_page.search('vitamin e')
search_results_page.verify_search_results_at_least(5)

number_of_product = 5
fifth_product_name_in_cart = search_results_page.get_product_name(number_of_product)
search_results_page.change_to_list_view()
fifth_product = search_results_page.add_to_cart(number_of_product)

cart_page = fifth_product.open_cart_page()
checkout_page = cart_page.open_checkout_page()
fifth_product_name_in_checkout = checkout_page.get_product_name(1)

assert fifth_product_name_in_cart == fifth_product_name_in_checkout, f'Product names are different'
