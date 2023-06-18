from selene import browser, by, be, have, config

from rozetka_home_page import RozetkaHomePage

home_page = RozetkaHomePage().open()
login_modal = home_page.open_login_modal()
login_modal.verify_that_login_modal_opened()
home_page = login_modal.close_modal()
