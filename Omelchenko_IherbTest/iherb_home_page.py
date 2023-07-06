from selene import browser, by, be

from Omelchenko_iHerbTest.iherb_login_landing_page import IherbLoginLandingPage
from Omelchenko_iHerbTest.iherb_search_results_page import IHerbSearchResultsPage
from Omelchenko_iHerbTest.iherb_site_preference_modal import IherbSitePreferenceModal


class IherbHomePage:

    def open(self):
        browser.open_url('https://www.iherb.com/')
        return self

    def open_site_preference_modal(self) -> IherbSitePreferenceModal:
        site_preference_button = browser.element(by.xpath("//div[@class='country-select']"))
        site_preference_button.wait.for_(be.visible)
        site_preference_button.click()
        return IherbSitePreferenceModal()

    def search(self, search_keyword) -> IHerbSearchResultsPage:
        search_box = browser.element(by.xpath("//input[@id='txtSearch']"))
        search_box.wait.for_(be.visible and be.blank)
        search_box.type(search_keyword).press_enter()
        return IHerbSearchResultsPage()

    def open_login_landing_page(self) -> IherbLoginLandingPage:
        browser.element(by.xpath('//*[@id="iherb-account"]/div/span/a')).click()
        return IherbLoginLandingPage()
