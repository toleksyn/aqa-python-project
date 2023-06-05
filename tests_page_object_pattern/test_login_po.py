from selene import browser, by, be, have, config

from rozetka_home_page import RozetkaHomePage
from rozetka_home_page import LoginModal
from login_modal import LoginModalOpened

def test_rozetka_search_po():
    config.timeout = 40

    home_page = RozetkaHomePage().open()
<<<<<<< HEAD
    login_modal = LoginModal().verify_opening_login_modal()
    login_modal_opened_state = LoginModalOpened().verify_that_login_modal_opened()
    login_modal_close = LoginModalOpened().close_modal()
    login_modal_closed_state = LoginModal().verify_that_modal_closed()
=======

    login_modal = LoginModal()

    login_modal.open = RozetkaHomePage().open_login_modal()
    login_modal.verify_login_modal_elements()

    login_modal.close_modal()
    login_modal.verify_modal_closing()
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71
