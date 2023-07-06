# Open iherb home page
# Search for ‘vitamin e’
# Verify at least 5 products are displayed
# Save the name of 5th product, add it to the cart
# Verify it’s added.
# Proceed to the checkout page.
# Verify the product name on checkout page is the same as in step 4.
from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage

home_page = IherbHomePage().open()

site_preference_drawer = home_page.open_site_preference_modal()
home_page = site_preference_drawer.change_language('English')

home_page.open_login_landing_page().log_in_with_iherb_account('roman.omelchenko@external.iherb.com', 'Qwertyuio?')

search_results_page = home_page.search('vitamin e')
search_results_page.verify_that_search_results_have_size_at_least(5)

product_number = 5
product_name = search_results_page.get_product_name(product_number)
cart_modal = search_results_page.add_to_cart_in_grid_view(product_number)

cart_page = cart_modal.open_cart_page()
checkout_page = cart_page.open_checkout_page_while_logged_in()
checkout_page.select_shipping_address(1)

product_name_on_checkout = checkout_page.get_product_name(1)

assert product_name == product_name_on_checkout, f'Product names are not equal'
