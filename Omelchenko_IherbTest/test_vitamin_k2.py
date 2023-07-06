# Open iherb home page
# Search for ‘vitamin k2’
# Verify at least 5 products are displayed
# In the filter section, check the NOW Foods checkbox
# Add 3rd product to the shopping cart
# In the shopping cart verify the name and price of added product are correct
# Click on 'Proceed to checkout'
# Verify the login page is open
# Login with the test account and try to complete the purchase.
# Add needed verifications steps (I don't have access to the test account)
from selene import browser

from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage


browser.config.timeout = 30
home_page = IherbHomePage().open()

site_preference_drawer = home_page.open_site_preference_modal()
home_page = site_preference_drawer.change_language('English')

search_results_page = home_page.search('vitamin k2')
search_results_page.verify_that_search_results_have_size_at_least(5)

filter_name = 'NOW Foods'
search_results_page.set_brands_filter(filter_name)

product_number = 3
third_product_name = search_results_page.get_product_name(product_number)
third_product_price = search_results_page.get_original_product_price(product_number)
third_product = search_results_page.add_to_cart_in_grid_view(product_number)

cart_page = third_product.open_cart_page()
third_product_name_in_cart = cart_page.get_product_name(1)
third_product_price_in_cart = cart_page.get_product_price(1)

assert third_product_name == third_product_name_in_cart, f'Product names are not equal'
assert third_product_price == third_product_price_in_cart, f'Product names are not equal'

login_landing_page = cart_page.open_checkout_page_while_not_logged_in()
login_landing_page.verify_that_opened()
checkout_page = login_landing_page.log_in_on_checkout('roman.omelchenko@external.iherb.com', 'Qwertyuio?')
checkout_page.select_shipping_address(1)
checkout_page.confirm_credit_card('377 9369 6532 0690')
update_payment_page = checkout_page.place_order_with_invalid_card()
order_details_page = update_payment_page.open_order_details_page()

order_details_page.verify_order_number_displayed()
