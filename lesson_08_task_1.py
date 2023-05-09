from selene import browser, by, be, have

browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank) \
    .type('funny kitten').press_enter()
browser.element(by.xpath('//h3[contains(text(), "kitten")]')).should(have.text('kitten'))
