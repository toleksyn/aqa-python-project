from selene import browser

from iherbtestvenv.iherb_home_page import IherbHomePage

def test_search_vitamin_e():
    browser.config.timeout = 40

    home_page = IherbHomePage().open()

    site_preference_modal = home_page.open_site_preference_modal()
    site_preference_modal.select_language('English')

    home_page.open_sign_in_page().log_in(login="auto-tests@yopmail.com", password="Test1234!")

    search_results_page = home_page.search('vitamin e')
    search_results_page.verify_search_results_at_least(5)

    product_number = 5
    fifth_product_name = search_results_page.get_product_name(product_number)
    fifth_product = search_results_page.add_product_to_cart(product_number)

    cart_page = fifth_product.open_cart_page()

    cart_page.verify_product_added_to_the_cart(1)

    checkout_page = cart_page.proceed_to_checkout()
    fifth_product_name_in_checkout = checkout_page.get_product_name(1)

    assert fifth_product_name == fifth_product_name_in_checkout, f"The product name on the Cart page does not match the product`s name on the Checkout page"