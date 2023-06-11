from rozetka_home_page import HomePage

home_page = HomePage().open()

login_popup = home_page.open_login_popup()
login_popup.verify_opened()

home_page = login_popup.close()
home_page.verify_closed()
