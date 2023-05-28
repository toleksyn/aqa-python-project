from selene import browser, by, be, have
from selene import config
import pytest

from rozetka_home_page import RozetkaHomePage
from login_modal import LoginModal

def test_rozetka_search_po():
    config.timeout = 40

    home_page = RozetkaHomePage().open()

    login_modal = LoginModal()

    login_modal.open = RozetkaHomePage().open_login_modal()
    login_modal.verify_login_modal_elements()

    login_modal.close_modal()
    login_modal.verify_modal_closing()
