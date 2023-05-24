from selene import browser, by, be, have
from selene import config
import pytest

from rozetka_home_page import RozetkaHomePage
from login_modal import LoginModal

def test_rozetka_search_po():
    config.timeout = 40
# Open http://rozetka.com.ua home page
    home_page = RozetkaHomePage().open()
# Click on the user icon in the top right corner
    login_modal = LoginModal()
# Verify that the login modal is displayed
    login_modal.open = RozetkaHomePage().open_login_modal()
    login_modal.verify_email_field()
    login_modal.verify_password_field()
    login_modal.verify_login_button()
    login_modal.verify_register_button()
    login_modal.verify_facebook_button()
    login_modal.verify_google_button()
 # Close the login modal, verify it’s closed
    login_modal.close_modal()
    login_modal.verify_modal_closing()
