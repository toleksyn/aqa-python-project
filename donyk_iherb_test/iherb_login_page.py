from selene import browser, by, be, query


class LoginPage:

    def log_in(self, username, password):
        self.set_username(username)
        self.set_password(password)
        browser.element(by.xpath('//button[@value="login"]')).click()
        from iherb_home_page import HomePage
        return HomePage()

    def set_username(self, username):
        browser.element(by.xpath('//input[@name="Username"]')).type(username)
        return self

    def set_password(self, password):
        browser.element(by.xpath('//input[@type="password"]')).type(password)
        return self

    def get_error_message_text(self):
        return browser.element(by.xpath('//div[@class="error-message"]/span/ul/li')).get(query.text)

    def verify_that_opened(self):
        browser.element(by.xpath('//input[@name="Username"]')).should(be.visible)
        browser.element(by.xpath('//input[@type="password"]')).should(be.visible)

    def log_in_on_cart(self, username, password):
        self.set_username(username)
        self.set_password(password)
        browser.element(by.xpath('//button[@value="login"]')).click()
        from iherb_cart_page import CartPage
        return CartPage()
