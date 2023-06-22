from pages.iherb_home_page import IherbHomePage


def test_iherb_the_third_task():
    # Open iherb home page
    home_page = IherbHomePage().open()

    # # Open login page
    login_page = home_page.open_the_login_page()

    # Set  non-existing username
    login_page.set_username("nonexisting@gmail.com")

    # Set non-existing password
    login_page.set_password("nonexistingpassword")

    # Verify the error message
    verifying_the_error_message = login_page.verify_that_error_message_is_displayed("Invalid email, phone number, or password")
