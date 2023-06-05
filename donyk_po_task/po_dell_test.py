from rozetka_home_page import HomePage

home_page = HomePage().open()

search_results_page = home_page.search('Dell')
search_results_page.verify_size_at_least(10)

fifth_product_name = search_results_page.get_product_name(5)
fifth_product_price = search_results_page.get_product_price(5)
add_to_basket_button = search_results_page.add_product_to_cart(5)

cart_popup = search_results_page.open_cart_popup()
added_product_name = cart_popup.get_product_name(5)
added_product_price = cart_popup.get_product_price(5)

assert added_product_name == fifth_product_name
assert added_product_price == fifth_product_price
