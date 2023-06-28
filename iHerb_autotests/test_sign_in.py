from selene import browser

from iherbtestvenv.iherb_home_page import IherbHomePage

def test_sign_in_with_incorrect_data():
    browser.config.timeout = 40

    home_page = IherbHomePage().open()

    site_preference_modal = home_page.open_site_preferences_modal()
    site_preference_modal.select_language('English')

    sign_in_page = home_page.open_sign_in_page()
    sign_in_page.sign_in(login="test11-test@yopmail.com", password="Test1234")
    sign_in_page.verify_that_error_message_displayed()