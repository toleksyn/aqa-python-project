# - Open http://rozetka.com.ua home page
# - Click on the user icon in the top right corner
# - Verify that the login modal is displayed
# - Close the login modal, verify it’s closed
from Omelchenko_RozetkaPageObjectTest.rozetka_home_page import RozetkaHomePage

home_page = RozetkaHomePage().open()

login_popup = home_page.open_login_popup()
login_popup.verify_that_opened()

home_page = login_popup.close()
home_page.verify_that_login_popup_closed()
