from rozetka_home_page import HomePage

home_page = HomePage().open()

search_results_page = home_page.search('iPhone')
search_results_page.verify_size_at_least(5)

third_product_price = search_results_page.get_product_price(3)
product_page = search_results_page.open_product_page(3)
product_page_price = product_page.get_product_price(3)

assert third_product_price == product_page_price
