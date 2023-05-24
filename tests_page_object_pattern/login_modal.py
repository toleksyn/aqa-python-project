from selene import browser, by, be, have
from selene import config
import pytest

class LoginModal:

    def verify_email_field(self):
        browser.element(by.xpath('//input[@type="email"]')).should(be.clickable)

    def verify_password_field(self):
        browser.element(by.xpath('//input[@type="password"]')).should(be.clickable)

    def verify_login_button(self):
        browser \
            .element(by.xpath('//button[@class="button button--large button--green auth-modal__submit ng-star-inserted"]')) \
            .should(be.clickable)

    def verify_register_button(self):
        browser \
            .element(by.xpath('//button[@class="auth-modal__register-link button button--link ng-star-inserted"]')) \
            .should(be.clickable)

    def verify_facebook_button(self):
        browser.element(by.xpath('//app-slider/div/button[1]')).should(be.clickable)

    def verify_google_button(self):
        browser.element(by.xpath('//app-slider/div/button[2]')).should(be.clickable)

    def close_modal(self):
        browser.element(by.xpath('//button[@class="modal__close"]')).click()

    def verify_modal_closing(self):
        browser.element(by.xpath('//div[@class="modal__content"]')).should_not(be.visible)