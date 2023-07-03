from selene import browser, by, be, have, query

class IherbSignInPage:

    def log_in(self, login, password):
        browser.element(by.xpath('//input[@id="username_input"]')).type(login)
        browser.element(by.xpath('//input[@class="form-text sign-in-password"]')).type(password)
        browser.element(by.xpath('//button[@id="sign_in_button"]')).click()
        from iherbtestvenv.iherb_home_page import IherbHomePage
        return IherbHomePage()

    def log_in_on_checkout(self, login, password):
        self.log_in(login, password)
        from iherbtestvenv.iherb_checkout_page import IherbCheckoutPage
        return IherbCheckoutPage()

    def verify_that_opened(self):
        browser.element(by.xpath("//input[@id='username_input']")).should(be.visible and be.blank)
        browser.element(by.xpath("//div[@class='form-row']/input[@type='password']")).should(be.visible and be.blank)

    def get_error_message_text(self):
        return browser.element(by.xpath("//div[@class='error-message']/span/ul/li")).get(query.text)

    def verify_confirm_dialog_form_open(self):
        browser.element(by.xpath('/div[@class="form confirm-dialog"]')).should(be.visible)

    def close_confirm_dialog_form(self):
        browser.element(by.xpath('//div[@class="exit"]')).click()
        from iherbtestvenv.iherb_home_page import IherbHomePage
        return IherbHomePage()