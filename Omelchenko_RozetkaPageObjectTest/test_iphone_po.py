# "- Open http://rozetka.com.ua home page
# - Search for ‘iPhone’
# - Verify that at least 5 result links are displayed and that each link text contains 'iPhone'
# - Verify the 3rd product has a price, save the price
# - Click on the 3rd product and verify that the stored price and price on product page is equal
from Omelchenko_RozetkaPageObjectTest.rozetka_home_page import RozetkaHomePage

# Task 1
home_page = RozetkaHomePage().open()

search_results = home_page.search('iPhone')
search_results.verify_search_results_have_size_at_least(5)

third_product_price = search_results.get_product_price(3)

third_product = search_results.open_product_description_page(3)
product_price_on_product_description_page = third_product.get_discounted_product_price()

assert third_product_price == product_price_on_product_description_page
