# Open iherb home page
# Search for ‘vitamin d’
# Verify at least 5 products are displayed
# In the filter section, check the NOW Foods checkbox
# Verify the all displayed products have ‘NOW Foods’ in the name
from selene import browser

from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage

browser.config.timeout = 40
home_page = IherbHomePage().open()

site_preference_modal = home_page.open_site_preference_modal()
home_page = site_preference_modal.change_language('English')

search_results = home_page.search('vitamin d')
search_results.verify_that_search_results_have_size_at_least(5)

filter_name = 'NOW Foods'
search_results.set_brands_filter(filter_name)

first_product_name = search_results.get_product_name(1)
last_product_name = search_results.get_product_name(48)
tenth_product_name = search_results.get_product_name(10)

assert first_product_name.startswith(filter_name), f'Product is not {filter_name} one'
assert last_product_name.startswith(filter_name), f'Product is not {filter_name} one'
assert tenth_product_name.startswith(filter_name), f'Product is not {filter_name} one'
