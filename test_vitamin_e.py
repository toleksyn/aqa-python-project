from iherbtestvenv.iherb_home_page import IherbHomePage

home_page = IherbHomePage().open()

sign_in_page = home_page.open_sign_in_page()
sign_in_with_correct_data = sign_in_page.sign_in(login="auto-tests@yopmail.com", password="Test1234!")

# close_confirm_dialog_form = sign_in_page.verify_confirm_dialog_form_open()
# sign_in_page.close_confirm_dialog_form()

site_preference_modal = home_page.open_site_preferences_modal()
home_page = site_preference_modal.select_language("English")
site_preference_modal = home_page.open_site_preferences_modal()
home_page = site_preference_modal.select_country("US - United States")

search_results_page = home_page.search('vitamin e')
search_results_page.verify_search_results_at_least(5)

fifth_product_name_on_search_page = search_results_page.get_product_name(5)
add_fifth_product_to_the_cart = search_results_page.add_product_to_cart(5)

modal_overlay = add_fifth_product_to_the_cart.verify_modal_open()

cart_page = add_fifth_product_to_the_cart.open_cart_page()

product_in_cart = cart_page.verify_product_added_to_the_cart(1)
product_name_in_cart = cart_page.get_product_name(1)

checkout_page = cart_page.proceed_to_checkout()
product_name_in_checkout = checkout_page.get_product_name(1)

assert product_name_in_cart == product_name_in_checkout, f"The product name on the Cart page does not match the product`s name on the Checkout page"