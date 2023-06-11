from rozetka_home_page import HomePage

home_page = HomePage().open()

search_results_page = home_page.search('iPhone')
search_results_page.verify_size_at_least(5)

number_of_product = 3

third_product_price = search_results_page.get_product_price(number_of_product)
product_page = search_results_page.open_product_page(number_of_product)
product_page_price = product_page.get_product_price(number_of_product)

assert third_product_price == product_page_price, f'Product prices are different'
