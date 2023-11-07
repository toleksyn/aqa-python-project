from selene import browser, by

from iherbtestvenv.iherb_site_preference_modal import IherbSitePreferenceModal
from iherbtestvenv.iherb_search_results_page import IherbSearchResultsPage
from iherbtestvenv.iherb_sign_in_page import IherbSignInPage

class IherbHomePage:

    def open(self):
        browser.open("https://www.iherb.com/")
        return self

    def search(self, keyword) -> IherbSearchResultsPage:
        browser \
            .element(by.xpath('//input[@class="iherb-header-search-input"]')) \
            .type(keyword) \
            .press_enter()
        return IherbSearchResultsPage()

    def open_sign_in_page(self) -> IherbSignInPage:
        browser.element(by.xpath('//*[@id="iherb-account"]/div/span/a')).click()
        return IherbSignInPage()

    def open_site_preference_modal(self) -> IherbSitePreferenceModal:
        browser.element(by.xpath('//div[@class="selected-country-wrapper"]')).click()
        return IherbSitePreferenceModal()