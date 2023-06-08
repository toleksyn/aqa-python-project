
def test_rozetka_login_modal(rozetka_home_page):

    rozetka_home_page.open()

    login_modal = rozetka_home_page.open_login_modal()
    login_modal.verify_that_login_modal_is_open()

    login_modal.close_login_modal()
    login_modal.verify_that_login_modal_is_closed()


