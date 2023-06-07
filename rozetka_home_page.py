from selene import browser, by

from pages.rozetka_login_modal import LoginModal
from pages.rozetka_search_results_page import RozetkaSearchResultsPage

class RozetkaHomePage:
    def open(self):
        browser.open("https://rozetka.com.ua/")

    def search(self, keyword):
        browser.element(by.name("search")).type(keyword).press_enter()
        return RozetkaSearchResultsPage()

    def open_login_modal(self) -> LoginModal:
        browser.element(by.xpath("//rz-user/button")).click()
        return LoginModal()
