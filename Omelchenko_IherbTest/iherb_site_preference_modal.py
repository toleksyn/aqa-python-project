from time import sleep

from selene import browser, by, be, have


class IherbSitePreferenceModal:

    def change_language(self, country_code):
        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).click()
        browser.element(by.xpath("//div[@class='item gh-dropdown-menu-item']/label[contains(text(), '{}')]"
                                 .format(country_code))).click()
        # browser.element(by.xpath("(//span[@class='gh-fake-input-value dropdown-text'])[2]/label"))\
        #     .should(have.text(country_code))
        browser.element(by.xpath("//div[@class='ccl-btn']/div/button[@class='save-selection gh-btn gh-btn-primary']"))\
            .click()
        from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage
        return IherbHomePage()
