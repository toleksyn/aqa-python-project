# Task 3
from iherb_home_page import HomePage

home_page = HomePage().open()

login_page = home_page.open_login_page()
login_page.log_in('test@yopmail.co', 'qwertyui')
error_message = login_page.get_error_message_text()

expected_error = 'Недійсна адреса електронної пошти, номер телефону або пароль'
assert error_message == expected_error, f'Error message is different'
