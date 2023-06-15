from selene import browser, by, query

class IherbLoginPage:
    def enter_login(self, non_existing_mail):
        browser.element(by.xpath('//input[@name="Username"]')).type(non_existing_mail)
        return self

    def enter_password(self, non_existing_password):
        browser.element(by.xpath('//input[@type="password"]')).type(non_existing_password).press_enter()
        return self

    def get_the_error_message_text(self, error_text):
        actual_error_message_text = browser.element(by.xpath(f'(//li[contains(text(),"{error_text}")])')).get(query.text)
        return actual_error_message_text
