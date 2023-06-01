from selene import browser, by, be

from rozetka_home_page import RozetkaHomePage


class LoginPopup:

    def open_login_popup(self):
        browser \
            .element(by.xpath('//input[@type="email"]')).should(be.clickable) \
            .element(by.xpath('//input[@type="password"]')).should(be.clickable) \
            .element(by.xpath('//button[@class="button button--large button--green auth-modal__submit ng-star-inserted"]')).should(be.clickable) \
            .element(by.xpath('//button[@class="auth-modal__register-link button button--link ng-star-inserted"]')).should(be.clickable)
        return LoginPopup

    def close_login_popup(self):
        browser.element(by.xpath('//button[@class="modal__close"]')).click()
        #from rozetka_home_page import RozetkaHomePage
        return RozetkaHomePage

    def verify_that_login_popup_is_closed(self):
        browser.element(by.xpath('//input[@type="password"]')).should(be.disabled)
        return RozetkaHomePage
