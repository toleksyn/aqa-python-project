# 1 Task
from iherb_home_page import HomePage

home_page = HomePage().open()

search_results_page = home_page.search('vitamin a')
search_results_page.verify_search_results_at_least(5)

product_number = 5
fifth_product_reviews_count = search_results_page.get_product_reviews_count(product_number)
product_page = search_results_page.open_product_page(product_number)
product_page_reviews_count = product_page.get_product_reviews_count()

assert fifth_product_reviews_count == product_page_reviews_count, f'Product reviews count are different'
