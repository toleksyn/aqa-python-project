from selene import browser, by, be, have, config

from rozetka_home_page import RozetkaHomePage
from rozetka_home_page import LoginModal
from login_modal import LoginModalOpened

def test_rozetka_search_po():
    config.timeout = 40

    home_page = RozetkaHomePage().open()
    login_modal = LoginModal().verify_opening_login_modal()
    login_modal_opened_state = LoginModalOpened().verify_that_login_modal_opened()
    login_modal_close = LoginModalOpened().close_modal()
    login_modal_closed_state = LoginModal().verify_that_modal_closed()