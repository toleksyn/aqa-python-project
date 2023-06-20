from selene import browser, by, be

from Omelchenko_iHerbTest.iherb_login_landing_page import LoginLandingPage
from Omelchenko_iHerbTest.iherb_search_results_page import IHerbSearchResultsPage
from Omelchenko_iHerbTest.iherb_site_preference_modal import IherbSitePreferenceModal


class IherbHomePage:

    def open(self):
        browser.open_url('https://www.iherb.com/')
        return self

    def open_site_preference_modal(self) -> IherbSitePreferenceModal:
        browser.element(by.xpath("//div[@class='country-select']")).click()
        return IherbSitePreferenceModal()

    def search(self, search_keyword) -> IHerbSearchResultsPage:
        browser.element(by.xpath("//input[@id='txtSearch']")).should(be.blank and be.visible)\
            .type(search_keyword).press_enter()
        return IHerbSearchResultsPage()

    def open_login_landing_page(self) -> LoginLandingPage:
        browser.element(by.xpath("//div[@class='iherb-header-account-sign-in']/span/a")).click()
        return LoginLandingPage()