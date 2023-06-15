from selene import browser, by, have


class LoginLandingPage:

    def log_in_with_iherb_account(self, username, password):
        self.set_username(username)
        self.set_password(password)
        browser.element(by.xpath("//button[@id='sign_in_button']")).click()
        from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage
        return IherbHomePage()

    def set_username(self, username):
        browser.element(by.xpath("//input[@id='username_input']")).type(username)

    def set_password(self, password):
        browser.element(by.xpath("//div[@class='form-row']/input[@type='password']")).type(password)

    def verify_that_error_message_displayed(self):
        browser.element(by.xpath("//div[@class='error-message']/span/ul/li"))\
            .should(have.text('Invalid email, phone number, or password'))

