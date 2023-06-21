from iherbtestvenv.iherb_home_page import IherbHomePage

home_page = IherbHomePage().open()

site_preference_modal = home_page.open_site_preferences_modal()
home_page = site_preference_modal.select_language('English')

home_page = IherbHomePage().open()
sign_in_page = home_page.open_sign_in_page()
sign_in_with_incorrect_data = sign_in_page.sign_in(login="test-email@yopmail.com", password="Test1234")
error_message = sign_in_page.verify_that_error_message_displayed()