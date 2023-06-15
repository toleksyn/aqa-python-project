from pages.iherb_home_page import IherbHomePage
from pages.iherb_login_page import IherbLoginPage


def test_iherb_the_third_task():
    # Open iherb home page
    home_page = IherbHomePage()
    home_page.open()

    # Open login page
    home_page.open_the_login_page()

    # Enter non-existing email
    login_page = IherbLoginPage()
    login_page.enter_login("nonexisting@mail.com")

    # Enter non-existing password
    login_page.enter_password("nonexistingpassword")

    # Verify error message
    actual_error_message_text = login_page.get_the_error_message_text("Invalid email, phone number, or password")
    expected_error_message_text = "Invalid email, phone number, or password"

    assert actual_error_message_text == expected_error_message_text

