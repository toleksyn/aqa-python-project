from selene import browser, by, config

from iherbtestvenv.iherb_home_page import IherbHomePage

def test_iherb_search_po():
    config.timeout = 10

    home_page = IherbHomePage().open()
    sign_in_page = home_page.open_sign_in_page()
    sign_in_with_incorrect_data = sign_in_page.sign_in(login="test-email@yopmail.com", password="Test1234")
    error_message = sign_in_page.get_actual_error_message()
    assert error_message == 'Invalid email, phone number, or password', "Error message doesn't match"