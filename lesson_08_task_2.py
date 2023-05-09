from selene import browser, by, be, have

browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank) \
    .type('funny dogs').press_enter()
browser.all(by.xpath('//h3[contains(text(), "dogs")]')).should(have.size(9))
