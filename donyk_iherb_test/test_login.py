# Task 3
from iherb_home_page import HomePage

home_page = HomePage().open()

login_page = home_page.open_login_page()
login_page.login('test@yopmail.co', 'qwertyui')
login_page.verify_the_error_message()
