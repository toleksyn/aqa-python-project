from selene import config

from rozetka_home_page import RozetkaHomePage
from rozetka_login_popup import LoginPopup


def test_rozetka_login():
    config.timeout = 40

rozetka_home_page = RozetkaHomePage()
rozetka_home_page.open()

login_modal = LoginPopup()
login_modal.open = RozetkaHomePage().open_login_popup()
login_modal.open_login_popup()

login_modal.close_login_popup()
login_modal.verify_that_login_popup_is_closed()


test_rozetka_login()