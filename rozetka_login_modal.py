from selene import browser, by, be

class LoginModal:
    def verify_that_login_modal_is_open(self):
        email_input = browser.element(by.xpath('//input[@type="email"]'))
        password_input = browser.element(by.xpath('//input[@type="password"]'))

        email_input.should(be.visible)
        password_input.should(be.visible)
        return self

    def close_login_modal(self):
        browser.element(by.xpath('//button[@class="modal__close"]')).click()
        return self

    def verify_that_login_modal_is_closed(self):
        browser.element(by.xpath('//input[@type="password"]')).should(be.not_.visible)
        return self
