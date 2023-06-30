from selene import browser, by
from pages.iherb_home_page import IherbHomePage


class IherbSitePreferenceModal:
    def open_country_dropdown(self):
        browser.element(by.xpath('//div[@class="select-country gh-dropdown"]')).click()
        return IherbSitePreferenceModal()

    def set_country(self, country):
        browser.element(by.xpath(f'//div[@data-val=contains(text(),"")]')).click()
        return IherbSitePreferenceModal()

    def apply_site_preference(self):
        browser.element(by.xpath('//button[@class="save-selection gh-btn gh-btn-primary"]')).click()
        return IherbHomePage()
