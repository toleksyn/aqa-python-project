from selene import browser, by, be, have

class LoginModalOpened:

<<<<<<< HEAD
    def verify_that_login_modal_opened(self):
=======
    def verify_login_modal_elements(self):
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71
        browser \
            .element(by.xpath('//input[@type="email"]')).should(be.clickable) \
            .element(by.xpath('//input[@type="password"]')).should(be.clickable) \
            .element(by.xpath('//button[@class="button button--large button--green auth-modal__submit ng-star-inserted"]')).should(be.clickable) \
            .element(by.xpath('//button[@class="auth-modal__register-link button button--link ng-star-inserted"]')).should(be.clickable) \
            .element(by.xpath('//app-slider/div/button[1]')).should(be.clickable) \
            .element(by.xpath('//app-slider/div/button[2]')).should(be.clickable)
<<<<<<< HEAD
        return self
=======

        return LoginModal
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71

    def close_modal(self):
        browser.element(by.xpath('//button[@class="modal__close"]')).click()
        from rozetka_home_page import RozetkaHomePage
<<<<<<< HEAD
        return RozetkaHomePage()
=======

        return RozetkaHomePage

    def verify_modal_closing(self):
        browser.element(by.xpath('//div[@class="modal__content"]')).should_not(be.visible)
        from rozetka_home_page import RozetkaHomePage

        return RozetkaHomePage
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71
