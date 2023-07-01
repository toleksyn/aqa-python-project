from selene import browser, by, be, have, config

from rozetka_home_page import RozetkaHomePage

home_page = RozetkaHomePage().open()
login_modal = home_page.open_login_modal()
login_modal.verify_opened()
home_page = login_popup.close()
home_page.verify_that_login_popup_closed()
