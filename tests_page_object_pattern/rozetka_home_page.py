from selene import browser, by, be, have
from selene import config
import pytest

from rozetka_search_results_page import RozetkaSearchResultsPage
from login_modal import LoginModal

class RozetkaHomePage:

    def open(self):
        browser.driver().get("http://rozetka.com.ua")

    def search(self, keyword) -> RozetkaSearchResultsPage():
        browser \
            .element(by.name('search')) \
            .type(keyword) \
            .press_enter()

        return RozetkaSearchResultsPage()

    def open_login_modal(self) -> LoginModal():
        browser.element(by.xpath('//button[@class="header__button ng-star-inserted"]')).click()

        return LoginModal()
