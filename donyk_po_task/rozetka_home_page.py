from selene import browser, by, be
from rozetka_search_results_page import SearchResultsPage
from rozetka_login_popup import LoginPopup


class HomePage:

    def open(self):
        browser.open_url('http://rozetka.com.ua')

    def search(self, keyword):
        browser.element(by.xpath('//input[@name="search"]')).type(keyword).press_enter()
        return SearchResultsPage()

    def open_login_popup(self):
        browser.element(by.xpath('//button[@class="header__button ng-star-inserted"]')).click()
        return LoginPopup()

    def verify_login_popup_closed(self):
        browser.element(by.xpath('//div[@class="modal__content"]')).should_not(be.visible)