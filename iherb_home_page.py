from selene import browser, by
from pages.iherb_search_results_page import IherbSearchResultsPage

class IherbHomePage:
    def open(self):
        browser.open("https://www.iherb.com/")
        return self

    def search(self, keyword):
        browser.element(by.xpath("//input[@id='txtSearch']")).type(keyword).press_enter()
        return IherbSearchResultsPage()

    def open_the_login_page(self):
        browser.element(by.xpath('//a[@class="iherb-header-signed-out icon-header_signed-out sign-in tablet-icon-login-link"]')).click()
        return self
