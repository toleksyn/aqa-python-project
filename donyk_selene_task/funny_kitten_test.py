from selene import browser, by, be, have


# Task 1
browser.open_url("https://google.com")

search_box_input = browser.element(by.xpath("//textarea[@name='q']")).should(be.blank)
search_box_input.type('funny kitten').press_enter()

browser.all("//div[@id='rso']")[0].element(by.xpath('.//h3')).should(have.text('kitten'))