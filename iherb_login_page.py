from selene import browser, by, be

class IherbLoginPage:
    def set_username(self, username):
        browser.element(by.xpath('//input[@name="Username"]')).type(username)
        return self

    def set_password(self, password):
        browser.element(by.xpath('//input[@type="password"]')).type(password).press_enter()
        return self

    def verify_that_error_message_is_displayed(self, error_text):
        browser.element(by.xpath(f'(//li[contains(text(),"{error_text}")])')).should(be.visible)

