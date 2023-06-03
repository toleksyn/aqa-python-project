from selene import browser, by, be


class RozetkaLoginPopup:

    def verify_that_opened(self):
        browser.element(by.xpath('//*[@id="auth_email"]')).should(be.visible)
        browser.element(by.xpath('//*[@id="auth_pass"]')).should(be.visible)
        browser.element(by.xpath("//div[@class='form__row auth-modal__form-bottom']/button[1]")).should(be.clickable)

    def close(self):
        browser.element(by.xpath("//div[@class='modal__header']/button")).click()
        from Omelchenko_RozetkaPageObjectTest.rozetka_home_page import RozetkaHomePage
        return RozetkaHomePage()
