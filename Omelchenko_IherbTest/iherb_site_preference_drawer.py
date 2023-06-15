from time import sleep

from selene import browser, by, have


class IherbSitePreferenceDrawer:

    def change_language(self, country_code):
        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).click()
        browser.element(by.xpath("//div[@class='item gh-dropdown-menu-item']/label[contains(text(), '{}')]"
                                 .format(country_code))).click()
        browser.element(by.xpath("//div[@class='ccl-btn']/div/button[@class='save-selection gh-btn gh-btn-primary']"))\
            .click()
        from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage
        return IherbHomePage()
