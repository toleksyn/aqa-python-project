from selene import browser, by, have, be


class LoginPage:

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        browser.element(by.xpath('//button[@value="login"]')).click()
        from iherb_home_page import HomePage
        return HomePage()

    def set_username(self, username):
        browser.element(by.xpath('//input[@name="Username"]')).type(username)

    def set_password(self, password):
        browser.element(by.xpath('//input[@type="password"]')).type(password)

    def verify_the_error_message(self):
        browser.element(by.xpath('//div[@class="error-message"]/span/ul/li')).should(have.text("Недійсна адреса електронної пошти, номер телефону або пароль"))

    def verify_opened(self):
        browser.element(by.xpath('//input[@name="Username"]')).should(be.visible)
        browser.element(by.xpath('//input[@type="password"]')).should(be.visible)

    def login_cart(self, username, password):
        self.set_username(username)
        self.set_password(password)
        browser.element(by.xpath('//button[@value="login"]')).click()
        from iherb_cart_page import CartPage
        return CartPage()
