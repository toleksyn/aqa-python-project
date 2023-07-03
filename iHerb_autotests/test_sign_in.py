from selene import browser

from iherbtestvenv.iherb_home_page import IherbHomePage

def test_sign_in_with_incorrect_data():
    browser.config.timeout = 20

    home_page = IherbHomePage().open()

    site_preference_modal = home_page.open_site_preference_modal()
    site_preference_modal.select_language('English')

    sign_in_page = home_page.open_sign_in_page()
    sign_in_page.log_in("incorrect_test_email@yopmail.com", "Test1234")

    error_message = sign_in_page.get_error_message_text()

    assert error_message == 'Invalid email, phone number, or password', f'Error message does not match the required'