# Open iherb home page
# Click the ‘Sign In’ button
# Try to sign in with non existing credentials
# Verify that the error message is displayed ‘Invalid email, phone number, or password’
from time import sleep

from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage


home_page = IherbHomePage().open()

site_preference_modal = home_page.open_site_preference_modal()
home_page = site_preference_modal.change_language('English')
sleep(3)
login_landing_page = home_page.open_login_landing_page()
login_landing_page.log_in_with_iherb_account('invalid_credentials@yopmail.com', '123456789')
login_landing_page.verify_that_error_message_displayed()

