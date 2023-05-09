from selene import browser, by, be, have

browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank) \
    .type('Selene').press_enter()
browser.element(by.xpath('//h3[contains(text(), "Selene")]')).should(have.text("Selene"))
browser.element('//img[@class="jfN4p"]').click()
browser.element(by.name('q')).should(be.blank)
