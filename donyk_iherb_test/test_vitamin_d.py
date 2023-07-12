# 2 Task
from iherb_home_page import HomePage

home_page = HomePage().open()

search_results_page = home_page.search('vitamin d')
search_results_page.verify_search_results_at_least(5)

filter_name = 'Now Foods'
search_results_page.set_filter(filter_name)

first_product_name = search_results_page.get_product_name(1)
middle_product_name = search_results_page.get_product_name(24)
last_product_name = search_results_page.get_product_name(48)

assert first_product_name.startswith(filter_name), f"Product doesn't contain {filter_name} in the name"
assert middle_product_name.startswith(filter_name), f"Product doesn't contain {filter_name} in the name"
assert last_product_name.startswith(filter_name), f"Product doesn't contain {filter_name} in the name"
