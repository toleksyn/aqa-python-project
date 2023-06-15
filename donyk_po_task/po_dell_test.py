from rozetka_home_page import HomePage

home_page = HomePage().open()

search_results_page = home_page.search('Dell')
search_results_page.verify_size_at_least(10)

fifth_product_name = search_results_page.get_product_name(5)
fifth_product_price = search_results_page.get_product_price(5)
add_fifth_product_to_cart = search_results_page.add_to_cart(5)

cart_popup = search_results_page.open_cart_popup()
added_product_name = cart_popup.get_product_name(1)
added_product_price = cart_popup.get_product_price(1)

assert added_product_name == fifth_product_name, f'Product names are different'
assert added_product_price == fifth_product_price, f'Product prices are different'
