from selene import browser, by


class HomePage:

    def open(self):
        browser.open_url('https://www.iherb.com/')
        return self

    def search(self, keyword):
        browser.element(by.xpath('//input[@id="txtSearch"]')).type(keyword).press_enter()
        from iherb_search_results_page import SearchResultsPage
        return SearchResultsPage()

    def open_login_page(self):
        browser.element(by.xpath('//a[@class="iherb-header-signed-out icon-header_signed-out sign-in tablet-icon-login-link"]')).click()
        from iherb_login_page import LoginPage
        return LoginPage()

    def open_site_preference_popup(self):
        browser.element(by.xpath('//div[@class="country-select"]')).click()
        from iherb_site_preference_popup import SitePreferencePopup
        return SitePreferencePopup()
