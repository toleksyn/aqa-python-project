from selene import browser, by, have, be

class IherbSignInPage:

    def sign_in(self, login, password):
        browser.element(by.xpath('//input[@id="username_input"]')).type(login)
        browser.element(by.xpath('//input[@class="form-text sign-in-password"]')).type(password)
        browser.element(by.xpath('//button[@id="sign_in_button"]')).click()
        from iherbtestvenv.iherb_home_page import IherbHomePage
        return IherbHomePage()

    def verify_that_error_message_displayed(self):
        browser.element(by.xpath("//div[@class='error-message']/span/ul/li"))\
            .should(have.text('Invalid email, phone number, or password'))

    def verify_confirm_dialog_form_open(self):
        browser.element(by.xpath('/div[@class="form confirm-dialog"]')).should(be.visible)

    def close_confirm_dialog_form(self):
        browser.element(by.xpath('//div[@class="exit"]')).click()
        from iherbtestvenv.iherb_home_page import IherbHomePage
        return IherbHomePage()


