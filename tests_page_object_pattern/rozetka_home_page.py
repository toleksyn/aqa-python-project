from selene import browser, by, be, have

from rozetka_search_results_page import RozetkaSearchResultsPage
from login_modal import LoginModal

class RozetkaHomePage:

    def open(self):
        browser.driver().get("https://rozetka.com.ua/ua/")
        return self

    def search(self, keyword) -> RozetkaSearchResultsPage:
        browser \
            .element(by.name('search')) \
            .type(keyword) \
            .press_enter()
        return RozetkaSearchResultsPage()

    def open_login_modal(self) -> LoginModal:
        browser.element(by.xpath('//button[@class="header__button ng-star-inserted"]')).click()
        return LoginModal()

    def verify_that_login_popup_closed(self):
        browser.element(by.xpath("//input[@name='search']")).should(be.visible and be.clickable)
        browser.element(by.xpath("//app-slider/div/button[1]")).should(be.visible and be.clickable)
        browser.element(by.xpath("//app-slider/div/button[2]")).should(be.visible and be.clickable)
        browser.element(by.xpath("//rz-top-slider/ul/li/a")).should(be.visible and be.clickable)
