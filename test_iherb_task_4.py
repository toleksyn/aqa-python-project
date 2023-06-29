from pages.iherb_home_page import IherbHomePage


def test_iherb_the_fourth_task():
    home_page = IherbHomePage().open()

    login_page = home_page.open_the_login_page()

    login_page.set_username("sinfrenka+99@gmail.com")

    login_page.set_password("test101202")

    search_result_page = home_page.search("vitamin e")

    search_result_page.verify_search_results_at_least(5)

    name_from_search_page = search_result_page.get_product_name(5)

    search_result_page.hover_to_the_add_cart_button(5)
    adde_to_cart_modal = search_result_page.add_product_to_the_cart(5)

    cart_page = adde_to_cart_modal.open_the_cart_page()

    cart_page.verify_that_product_is_added_to_the_cart()

    checkout_page = cart_page.procced_to_checkout()

    product_name_from_checkout = checkout_page.get_product_name()

    assert name_from_search_page == product_name_from_checkout, f'Product names are not equal'
