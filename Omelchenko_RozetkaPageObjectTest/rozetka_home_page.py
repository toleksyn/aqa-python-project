from selene import browser, by, be

from Omelchenko_RozetkaPageObjectTest.rozetka_login_popup import RozetkaLoginPopup
from Omelchenko_RozetkaPageObjectTest.rozetka_search_results_page import RozetkaSearchResultsPage


class RozetkaHomePage:

    def open(self):
        browser.open_url('https://rozetka.com.ua/ua/')
        return self

    def search(self, search_keyword) -> RozetkaSearchResultsPage:
        search_field = browser.element(by.xpath("//input[@name='search']")).should(be.visible)
        search_field.type(search_keyword).press_enter()
        return RozetkaSearchResultsPage()

    def open_login_popup(self) -> RozetkaLoginPopup:
        browser.element(by.xpath("//rz-user/button")).click()
        return RozetkaLoginPopup()

    def verify_that_login_popup_closed(self):
        browser.element(by.xpath("//input[@name='search']")).should(be.visible and be.clickable)
        browser.element(by.xpath("//app-slider/div/button[1]")).should(be.visible and be.clickable)
        browser.element(by.xpath("//app-slider/div/button[2]")).should(be.visible and be.clickable)
        browser.element(by.xpath("//rz-top-slider/ul/li/a")).should(be.visible and be.clickable)
