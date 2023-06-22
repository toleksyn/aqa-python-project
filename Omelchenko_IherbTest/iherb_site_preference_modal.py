from selene import browser, by, have


class IherbSitePreferenceModal:

    def change_language(self, language):
        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).click()
        browser.element(by.xpath("//div[@class='item gh-dropdown-menu-item']/label[contains(text(), '{}')]"
                                 .format(language))).click()
        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).assure(have.text(language), timeout=15)
        browser.element(by.xpath("//div[@class='ccl-btn']/div/button[@class='save-selection gh-btn gh-btn-primary']"))\
            .click()
        from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage
        return IherbHomePage()
