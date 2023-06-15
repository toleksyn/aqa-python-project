from selene import browser, by

from Omelchenko_iHerbTest.iherb_login_landing_page import LoginLandingPage
from Omelchenko_iHerbTest.iherb_search_results_page import IHerbSearchResultsPage
from Omelchenko_iHerbTest.iherb_site_preference_drawer import IherbSitePreferenceDrawer


class IherbHomePage:

    def open(self):
        browser.open_url('https://www.iherb.com/')
        return self

    def open_site_preference_drawer(self) -> IherbSitePreferenceDrawer:
        browser.element(by.xpath("//div[@class='country-select']")).click()
        return IherbSitePreferenceDrawer()

    def search(self, search_keyword) -> IHerbSearchResultsPage:
        browser.element(by.xpath("//input[@id='txtSearch']")).type(search_keyword).press_enter()
        return IHerbSearchResultsPage()

    def open_login_page(self) -> LoginLandingPage:
        browser.element(by.xpath("//div[@class='iherb-header-account-sign-in']/span/a")).click()
        return LoginLandingPage()
