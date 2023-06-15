# Open iherb home page
# Search for ‘vitamin d’
# Verify at least 5 products are displayed
# In the filter section, check the NOW Foods checkbox
# Verify the all displayed products have ‘NOW Foods’ in the name
from time import sleep

from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage


home_page = IherbHomePage().open()

# site_preference_drawer = home_page.open_site_preference_drawer()
# home_page = site_preference_drawer.change_language('English')

search_results = home_page.search('vitamin d')
search_results.verify_that_search_results_have_size_at_least(5)

search_results.set_brands_filter('NOW Foods')
search_results.verify_that_all_products_are_filtered_by('NOW Foods')
