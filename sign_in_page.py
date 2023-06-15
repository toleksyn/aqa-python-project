from selene import browser, by

class SignInPage:

    def sign_in(self, login, password):
        browser.element(by.xpath('//input[@id="username_input"]')).type(login)
        browser.element(by.xpath('//input[@class="form-text sign-in-password"]')).type(password)
        browser.element(by.xpath('//button[@id="sign_in_button"]')).click()
        return self

    def get_actual_error_message(self):
        browser.element(by.xpath('//div[@class="error-message"]')).get(str)
        return self