from selene import browser, by, be


class LoginPopup:

    def verify_opened(self):
        browser.element(by.xpath('//div[@class="modal__content"]')).should(be.visible)
        browser.element(by.xpath('//input[@id="auth_email"]')).should(be.visible)
        browser.element(by.xpath('//input[@id="auth_pass"]')).should(be.visible)
        browser.element(by.xpath(
            '//button[@class="button button--large button--green auth-modal__submit ng-star-inserted"]')).should(
            be.clickable)

    def close(self):
        browser.element(by.xpath('//button[@class="modal__close"]')).click()
        from rozetka_home_page import HomePage
        return HomePage()
