# - Open http://rozetka.com.ua home page
# - Click on the user icon in the top right corner
# - Verify that the login modal is displayed
# - Close the login modal, verify it’s closed
from Omelchenko_RozetkaPageObjectTest.rozetka_home_page import RozetkaHomePage

home_page = RozetkaHomePage()
home_page.open()
login_popup = home_page.open_login_popup()
login_popup.verify_that_login_popup_opened()
turned_back_to_home = login_popup.close()
turned_back_to_home.verify_that_login_popup_closed()
