from selene import browser, by

# from iherbtestvenv.ccl import CountryCurrencyLanguage
from iherbtestvenv.iherb_search_page import IherbSearchPage
from iherbtestvenv.sign_in_page import SignInPage

class IherbHomePage:

    def open(self):
        browser.open("https://www.iherb.com/")
        return self

    def search(self, keyword) -> IherbSearchPage:
        browser \
            .element(by.xpath('//input[@class="iherb-header-search-input"]')) \
            .type(keyword) \
            .press_enter()
        return IherbSearchPage()

    def open_sign_in_page(self) -> SignInPage:
        browser.element(by.xpath('//*[@id="iherb-account"]/div/span/a')).click()
        return SignInPage()

    # def open_ccl(self):
    #     browser.element(by.xpath('//div[@class="selected-country-wrapper"]')).click()
    #     return CountryCurrencyLanguage()