# 2 Task
from iherb_home_page import HomePage
from time import sleep

home_page = HomePage().open()

search_results_page = home_page.search('vitamin d')
search_results_page.verify_size_at_least(5)

search_results_page.set_filter('NOW Foods')
sleep(5)

first_product = search_results_page.get_product_name(1)
middle_product = search_results_page.get_product_name(24)
last_product = search_results_page.get_product_name(48)

assert first_product.startswith("Now Foods"), f"Product doesn't contain 'Now Foods' in the name"
assert middle_product.startswith("Now Foods"), f"Product doesn't contain 'Now Foods' in the name"
assert last_product.startswith("Now Foods"), f"Product doesn't contain 'Now Foods' in the name"
