from selene import have

from iherbtestvenv.iherb_home_page import IherbHomePage

home_page = IherbHomePage().open()

site_preference_modal = home_page.open_site_preferences_modal()
home_page = site_preference_modal.select_language('English')

search_results_page = home_page.search('vitamin d')
search_results_page.verify_search_results_at_least(5)

search_results_page.set_brands_filter('NOW Foods')

first_product_name = search_results_page.get_product_name(1)
last_product_name = search_results_page.get_product_name(48)
twenty_fourth_product_name = search_results_page.get_product_name(24)

assert first_product_name.should(have.text("NOW Foods")), f"The product has no 'Now Foods' name"
assert last_product_name.should(have.text("NOW Foods")), f"The product has no 'Now Foods' name"
assert twenty_fourth_product_name.should(have.text("NOW Foods")), f"The product has no 'Now Foods' name"