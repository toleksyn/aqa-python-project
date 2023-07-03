# Open iherb home page
# Click the ‘Sign In’ button
# Try to sign in with non existing credentials
# Verify that the error message is displayed ‘Invalid email, phone number, or password’
from selene import browser

from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage

browser.config.timeout = 30
home_page = IherbHomePage().open()

site_preference_modal = home_page.open_site_preference_modal()
home_page = site_preference_modal.change_language('English')

login_landing_page = home_page.open_login_landing_page()
login_landing_page.log_in_with_iherb_account('invalid_credentials@yopmail.com', '123456789')

error_message = login_landing_page.get_error_message_text()

test_error = 'Invalid email, phone number, or password'
assert error_message == test_error, f'Error message does not match the required'
