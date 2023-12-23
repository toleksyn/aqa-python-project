# Open iherb home page
# Search for ‘vitamin a’
# Verify at least 5 products are displayed
# Save the reviews count for 5th product and click on it
# Verify the reviews count on product page is the same as in the previous step
from selene import browser

from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage

browser.config.timeout = 40
home_page = IherbHomePage().open()

site_preference_modal = home_page.open_site_preference_modal()
home_page = site_preference_modal.change_language('English')

search_results_page = home_page.search('vitamin a')
search_results_page.verify_that_search_results_have_size_at_least(5)

product_number = 5
product_reviews_amount = search_results_page.get_product_reviews_amount(product_number)
product_details_page = search_results_page.open_product_details_page(product_number)

product_details_reviews_amount = product_details_page.get_product_reviews_amount()

assert product_reviews_amount == product_details_reviews_amount, f'Product reviews amount is not equal'