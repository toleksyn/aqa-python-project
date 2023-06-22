from pages.iherb_home_page import IherbHomePage


def test_iherb_the_fourth_task():
    # Open iherb home page
    home_page = IherbHomePage().open()

    # Set site preference
    site_preference = home_page.open_site_preference()
    site_preference.open_country_dropdown()
    site_preference.set_country("US")
    site_preference.apply_site_preference()

    # Open the login page
    login_page = home_page.open_the_login_page()

    # Set username
    login_page.set_username("sinfrenka+99@gmail.com")

    # Set password
    login_page.set_password("test101202")

    # Search for ‘vitamin d’
    search_result_page = home_page.search("vitamin e")

    # Verify at least 5 products are displayed
    search_result_page.verify_search_results_at_least(5)

    # Get name from search page
    name_from_search_page = search_result_page.get_product_name_from_search_page(5)

    # Add to cart
    adde_to_cart_modal = search_result_page.add_product_to_the_cart(5)

    # Open the cart page
    cart_page = adde_to_cart_modal.open_the_cart_page()

    # Verify that product is added to the cart
    cart_page.verify_that_product_is_added_to_the_cart()

    # Open the checkout page
    checkout_page = cart_page.procced_to_checkout()

    # Expand product panel
    checkout_page.expand_product_panel()

    # Get name product from checkout
    product_name_from_checkout = checkout_page.get_product_name_from_checkout()

    assert name_from_search_page == product_name_from_checkout, f'Product names are not equal'







