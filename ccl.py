# This class is not used yet - needed to be discussed

from selene import browser, by, be, have, config

class CountryCurrencyLanguage:

    def open_select_your_language_drop_down(self):
        browser.element(by.xpath('//input[@id="CurrentLanguageCode"]')).click()
        return self

    def select_language(self):
        return browser.element(by.xpath('//div[@data-val="en-US"]')).should(be.selected)

    def save_site_preferences(self):
        browser.element(by.xpath('//button[@class="save-selection gh-btn gh-btn-primary"]')).click()
        return self