from selene import browser, by, be, have

from rozetka_search_results_page import RozetkaSearchResultsPage
from login_modal import LoginModalOpened

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

class LoginModal:

    def verify_opening_login_modal(self):
        browser.element(by.xpath('//button[@class="header__button ng-star-inserted"]')).click()
        return self

<<<<<<< HEAD
    def verify_that_modal_closed(self):
        browser.element(by.xpath('//div[@class="modal__content"]')).should_not(be.visible)
        from rozetka_home_page import RozetkaHomePage
        return RozetkaHomePage()
=======
        return LoginModal()
>>>>>>> a966a406169566376a61c2aaafdc9de0f1b2bb71
