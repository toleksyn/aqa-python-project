from selene import browser, by, be


class IherbSitePreferenceModal:

    def change_country(self, country_code):
        browser.element(by.xpath("//input[@class='search-input gh-dropdown-search gh-fake-input']")).click()
        country_list = browser.element(by.xpath("//div[@class='menu search-list gh-dropdown-menu open']"))
        country_list.wait.for_(be.visible)
        browser.element(by.xpath("//div[@class='gh-dropdown-menu-item item popular']/label[contains(text(), '{}')]"
                                 .format(country_code))).click()
        country_list.wait.untill(be.hidden)
        browser.element(by.xpath("(//*[@class='ccl-btn']//button)[2]")).click()
        browser.element(by.xpath("//*[@class='selection-list-wrapper']")).wait.until(be.hidden)
        from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage
        return IherbHomePage()

    def change_language(self, language):
        browser.element(by.xpath("//*[@class='selection-list-wrapper']")).wait.until(be.visible)
        browser.element(by.xpath("//input[@class='search-input gh-dropdown-search gh-fake-input']")).click()
        country_list = browser.element(by.xpath("//div[@class='menu search-list gh-dropdown-menu open']"))
        country_list.wait.for_(be.visible)
        browser.element(by.xpath("//div[@class='gh-dropdown-menu-item item popular']/label[contains(text(), '{}')]"
                                 .format(language))).click()
        country_list.wait.untill(be.hidden)
        browser.element(by.xpath("//div[@class='ccl-header']")).wait.until(be.visible)
        browser.element(by.xpath("(//*[@class='ccl-btn']//button)[2]")).click()
        browser.element(by.xpath("//*[@class='selection-list-wrapper']")).wait.until(be.hidden)
        from Omelchenko_iHerbTest.iherb_home_page import IherbHomePage
        return IherbHomePage()
