# Open iherb home page
# Search for ‘vitamin e’
# Verify at least 5 products are displayed
# Save the name of 5th product, add it to the cart
# Verify it’s added.
# Proceed to the checkout page.
# Verify the product name on checkout page is the same as in step 4.
from time import sleep

from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage


home_page = IherbHomePage().open()

# site_preference_drawer = home_page.open_site_preference_drawer()
# home_page = site_preference_drawer.change_language('English')
home_page.open_login_page().log_in_with_iherb_account('roman.omelchenko@external.iherb.com', 'Qwertyuio?')

search_results = home_page.search('vitamin e')
search_results.verify_that_search_results_have_size_at_least(5)

product_number = 5
fifth_product_name = search_results.get_product_name(product_number)
fifth_product = search_results.add_to_cart(product_number)

# cart_page = fifth_product.verify_product_added_to_cart().navigate_to_cart_page()
# checkout_page = cart_page.navigate_to_checkout_page()
# fifth_product_name_on_checkout = checkout_page.get_product_name()

# assert fifth_product_name == fifth_product_name_on_checkout, f'Product names are not equal'