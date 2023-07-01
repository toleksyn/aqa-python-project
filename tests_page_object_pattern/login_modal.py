from selene import browser, by, be, have

class LoginModal:

    def verify_opened(self):
        browser.element(by.xpath('//input[@type="email"]')).should(be.clickable)
        browser.element(by.xpath('//input[@type="password"]')).should(be.clickable)
        browser.element(by.xpath('//button[@class="button button--large button--green auth-modal__submit ng-star-inserted"]')).should(be.clickable)
        browser.element(by.xpath('//button[@class="auth-modal__register-link button button--link ng-star-inserted"]')).should(be.clickable)
        browser.element(by.xpath('//app-slider/div/button[1]')).should(be.clickable)
        browser.element(by.xpath('//app-slider/div/button[2]')).should(be.clickable)
    
    def close(self):
        browser.element(by.xpath("//div[@class='modal__header']/button")).click()
        from Omelchenko_RozetkaPageObjectTest.rozetka_home_page import RozetkaHomePage
        return RozetkaHomePage()
