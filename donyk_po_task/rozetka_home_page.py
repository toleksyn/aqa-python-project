from selene import browser, by, be


class HomePage:

    def open(self):
        browser.open_url('http://rozetka.com.ua')
        return self

    def search(self, keyword):
        browser.element(by.xpath('//input[@name="search"]')).type(keyword).press_enter()
        from rozetka_search_results_page import SearchResultsPage
        return SearchResultsPage()

    def open_login_popup(self):
        browser.element(by.xpath('//button[@class="header__button ng-star-inserted"]')).click()
        from rozetka_login_popup import LoginPopup
        return LoginPopup()

    def verify_closed(self):
        browser.element(by.xpath('//div[@class="modal__content"]')).should_not(be.visible)
        
