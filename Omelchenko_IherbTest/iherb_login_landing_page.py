from selene import browser, by, be, query


class IherbLoginLandingPage:

    def log_in_with_iherb_account(self, username, password):
        self.log_in(username, password)
        from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage
        return IherbHomePage()

    def log_in_on_checkout(self, username, password):
        self.log_in(username, password)
        from Omelchenko_iHerbTest.iherb_checkout_page import IherbCheckoutPage
        return IherbCheckoutPage()

    def log_in(self, username, password):
        self.set_username(username)
        self.set_password(password)
        browser.element(by.xpath("//button[@id='sign_in_button']")).wait.for_(be.visible)
        browser.element(by.xpath("//button[@id='sign_in_button']")).click()

    def set_username(self, username):
        browser.element(by.xpath("//input[@id='username_input']")).type(username)
        return self

    def set_password(self, password):
        browser.element(by.xpath("//div[@class='form-row']/input[@type='password']")).type(password)
        return self

    def get_error_message_text(self):
        browser.element(by.xpath("//div[@class='error-message']/span/ul/li")).get(query.text)

    def verify_that_opened(self):
        browser.element(by.xpath("//input[@id='username_input']")).should(be.visible and be.blank)
        browser.element(by.xpath("//div[@class='form-row']/input[@type='password']")).should(be.visible and be.blank)


