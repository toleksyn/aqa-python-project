from selene import browser, by, be

from pages.iherb_search_results_page import IherbSearchResultsPage
from pages.iherb_login_page import IherbLoginPage
from pages.iherb_site_preference_modal import IherbSitePreferenceModal

class IherbHomePage:
    def open(self):
        browser.open("https://www.iherb.com/")
        return self

    def search(self, keyword):
        browser.element(by.xpath("//input[@id='txtSearch']")).type(keyword).press_enter()
        return IherbSearchResultsPage()

    def open_the_login_page(self):
        browser.element(by.xpath('//a[contains(@class, "sign-in")]')).should(be.visible).click()
        return IherbLoginPage()

    def open_site_preference(self):
        browser.element(by.xpath('//div[@class="country-select"]')).should(be.visible).click()
        return IherbSitePreferenceModal()
