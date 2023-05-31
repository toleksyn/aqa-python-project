from rozetka_home_page import HomePage

home_page = HomePage()
home_page.open()

login_popup = home_page.open_login_popup()
login_popup.verify_login_popup_opened()

close_login = login_popup.close_popup()
close_login.verify_login_popup_closed()
