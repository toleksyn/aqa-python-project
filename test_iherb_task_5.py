from pages.iherb_home_page import IherbHomePage

def test_iherb_the_fifth_task():

    home_page = IherbHomePage().open()

    search_result_page = home_page.search("vitamin k2")

    search_result_page.verify_search_results_at_least(5)

    search_result_page.set_the_filter("NOW Foods")

    product_name_from_search_result = search_result_page.get_product_name(3)

    search_result_page.hover_to_the_add_cart_button(3)
    iherb_cart_modal = search_result_page.add_product_to_the_cart(3)

    product_name_from_cart_modal = iherb_cart_modal.get_product_name()

    assert product_name_from_search_result == product_name_from_cart_modal, f'Product names are not equal'

    login_page = iherb_cart_modal.open_the_cart_page().procced_to_checkout()

    login_page.set_username("sinfrenka+99@gmail.com")

    login_page.set_password("test101202")

    from pages.iherb_checkout_page import IherbCheckoutPage
    checkout_page = IherbCheckoutPage().re_enter_credit_card_number("4847 1801 5297 2716").approve_credit_card_number
    checkout_page.place_oredr()
