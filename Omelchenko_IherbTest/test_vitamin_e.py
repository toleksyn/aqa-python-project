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

search_results = home_page.search('vitamin e')
search_results.verify_that_search_results_have_size_at_least(5)

product_number = 5
fifth_product_name = search_results.get_product_name(product_number)
search_results.change_to_list_view()
fifth_product = search_results.add_to_cart(product_number)

cart_page = fifth_product.open_cart_page()
checkout_page = cart_page.open_checkout_page()
checkout_page.select_shipping_address(1)

fifth_product_name_on_checkout = checkout_page.get_product_name(1)

assert fifth_product_name == fifth_product_name_on_checkout, f'Product names are not equal'