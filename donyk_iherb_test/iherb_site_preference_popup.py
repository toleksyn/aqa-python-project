from selene import browser, by


class SitePreferencePopup:

    def change_country(self, country, zip_code):
        browser.element(by.xpath('//div[@class="select-country gh-dropdown"]')).click()
        browser.element(by.xpath('//div[@class="gh-dropdown-menu-item item"]/label[contains(text(), "{}")]'.format(country))).click()
        browser.element(by.xpath('//div[@class="input-zipcode gh-input"]')).type(zip_code)
        browser.element(by.xpath('//button[@class="save-selection gh-btn gh-btn-primary"]')).click()
        from iherb_home_page import HomePage
        return HomePage()
