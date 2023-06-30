from pages.iherb_home_page import IherbHomePage


def test_iherb_the_third_task():

    home_page = IherbHomePage().open()

    login_page = home_page.open_the_login_page()

    login_page.set_username("nonexisting@gmail.com")

    login_page.set_password("nonexistingpassword")

    verifying_the_error_message = login_page.verify_that_error_message_is_displayed("Invalid email, phone number, or password")
