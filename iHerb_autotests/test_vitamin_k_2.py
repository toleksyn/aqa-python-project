# Several steps need to be discussed

from selene import browser

from iherbtestvenv.iherb_home_page import IherbHomePage

def test_search_vitamin_k_2():

    browser.config.timeout = 20

    home_page = IherbHomePage().open()

    site_preference_modal = home_page.open_site_preferences_modal()
    home_page = site_preference_modal.select_language('English')

    search_results_page = home_page.search('vitamin k2')
    search_results_page.verify_search_results_at_least(5)

    filter_name = 'NOW Foods'
    search_results_page.set_brands_filter(filter_name)

    product_number = 3
    third_product_name = search_results_page.get_product_name(product_number)
    third_product_price = search_results_page.get_original_product_price(product_number)
    third_product = search_results_page.add_product_to_cart(product_number)

    cart_page = third_product.open_cart_page()
    third_product_name_in_cart = cart_page.get_product_name(1)
    third_product_price_in_cart = cart_page.get_product_price(1)

    assert third_product_name == third_product_name_in_cart, f'Product names are not equal'
    assert third_product_price == third_product_price_in_cart, f'Product prices are not equal'

    login_page = home_page.open_sign_in_page()
    login_page.verify_that_opened()
    checkout_page = login_page.sign_in(login="auto-tests@yopmail.com", password="Test1234!")
    checkout_page.place_order()