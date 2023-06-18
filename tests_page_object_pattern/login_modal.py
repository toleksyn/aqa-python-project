from selene import browser, by, be, have

class LoginModal:

    def verify_that_login_modal_opened(self):
        browser \
            .element(by.xpath('//input[@type="email"]')).should(be.clickable) \
            .element(by.xpath('//input[@type="password"]')).should(be.clickable) \
            .element(by.xpath('//button[@class="button button--large button--green auth-modal__submit ng-star-inserted"]')).should(be.clickable) \
            .element(by.xpath('//button[@class="auth-modal__register-link button button--link ng-star-inserted"]')).should(be.clickable) \
            .element(by.xpath('//app-slider/div/button[1]')).should(be.clickable) \
            .element(by.xpath('//app-slider/div/button[2]')).should(be.clickable)

    def close_modal(self):
        browser.element(by.xpath('//button[@class="modal__close"]')).click()
        from rozetka_home_page import RozetkaHomePage
        return RozetkaHomePage()
