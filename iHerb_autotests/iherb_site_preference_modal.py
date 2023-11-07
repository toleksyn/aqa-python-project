from selene import browser, by, be

class IherbSitePreferenceModal:

    def select_language(self, language):
        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).click()
        language_list = browser.element(by.xpath("//div[@class='menu search-list gh-dropdown-menu open']"))
        language_list.wait.for_(be.visible)
        browser.element(by.xpath("//div[@class='item gh-dropdown-menu-item']/label[contains(text(), '{}')]"
                                 .format(language))).click()
        language_list.wait.until(be.hidden)
        browser.element(by.xpath("(//*[@class='ccl-btn']//button)[2]")).click()
        browser.element(by.xpath("//*[@class='selection-list-wrapper']")).wait.until(be.hidden)
        from iherbtestvenv.iherb_home_page import IherbHomePage
        return IherbHomePage()