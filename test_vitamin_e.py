# The task is in Progress

from selene import browser, by, be, have, config

from iherbtestvenv.iherb_home_page import IherbHomePage
from iherb_modal_container import IherbModalContainer

def test_iherb_search_po(products=None):
    config.timeout = 40

    home_page = IherbHomePage().open()
    sign_in_page = home_page.open_sign_in_page()
    sign_in_with_correct_data = sign_in_page.sign_in(login="testfort_test_acc1@yopmail.com", password="Test1234!")

    results_page = home_page.search('vitamin e')
    results_page.verify_search_results_at_least(5)

    fifth_product_name = results_page.get_product_name(5)
    add_product_to_the_cart = results_page.add_product_to_the_cart(5).proceed_to_cart_page()
    add_product_to_the_cart.proceed_to_the_checkout_page()