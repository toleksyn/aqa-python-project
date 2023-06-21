from selene import browser, by, be

class IherbSitePreferenceModal:
    def select_country(self, country_code):
        browser.element(by.xpath("//div[@class='select-country gh-dropdown']")).wait_until(be.visible)
        browser.element(by.xpath("//div[@class='select-country gh-dropdown']")).click()
        browser.element(by.xpath(format("//div[@class='gh-dropdown-menu-item item']/label[contains(text(),'{}')]"\
                                        .format(country_code)))).click()
        browser.element(by.xpath('//button[@class="save-selection gh-btn gh-btn-primary"]')).click()

        from iherbtestvenv.iherb_home_page import IherbHomePage
        return IherbHomePage()

    def select_language(self, language):
        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).wait_until(be.visible)
        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).click()
        browser.element(by.xpath(format("//div[@class='item gh-dropdown-menu-item']/label[contains(text(),'{}')]"
                                 .format(language)))).click()
        browser.element(by.xpath('//button[@class="save-selection gh-btn gh-btn-primary"]')).click()

        from iherbtestvenv.iherb_home_page import IherbHomePage
        return IherbHomePage()

    def select_country_with_language(self, language, country_code):

        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).wait_until(be.visible)
        browser.element(by.xpath("//div[@class='select-language gh-dropdown']")).click()

        browser.element(by.xpath(format("//div[@class='item gh-dropdown-menu-item']/label[contains(text(), '{}')]". \
                                        format(language)))).click()

        browser.element(by.xpath("//div[@class='select-country gh-dropdown']")).wait_until(be.visible)
        browser.element(by.xpath("//div[@class='select-country gh-dropdown']")).click()
        browser.element(by.xpath(format("//div[@class='gh-dropdown-menu-item item popular']/label[contains(text(),'{}')]" \
                                        .format(country_code)))).click()

        browser.element(by.xpath('//button[@class="save-selection gh-btn gh-btn-primary"]')).click()

        from iherbtestvenv.iherb_home_page import IherbHomePage
        return IherbHomePage()