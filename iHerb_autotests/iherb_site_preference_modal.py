from selene import browser, by, be

class IherbSitePreferenceModal:

    def select_language(self, language):
        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).wait_until(be.visible)
        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).click()
        browser.element(by.xpath(format("//div[@class='item gh-dropdown-menu-item']/label[contains(text(),'{}')]"
                                 .format(language)))).click()
        browser.element(by.xpath('//button[@class="save-selection gh-btn gh-btn-primary"]')).click()
        from iherbtestvenv.iherb_home_page import IherbHomePage
        return IherbHomePage()