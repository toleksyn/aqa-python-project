from selene import browser, by, be, have, config

from rozetka_home_page import RozetkaHomePage

def test_rozetka_search_po():
    config.timeout = 40

    home_page = RozetkaHomePage().open()
    login_modal = home_page.open_login_modal()
    login_modal.verify_that_login_modal_opened()
    home_page = login_modal.close_modal()
    home_page.verify_that_modal_closed()
