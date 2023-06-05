from rozetka_home_page import HomePage

home_page = HomePage().open()

login_popup = home_page.open_login()
login_popup.verify_opened()

close = login_popup.close()
close.verify_closed()
