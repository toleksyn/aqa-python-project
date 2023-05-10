from selene import browser, by, be, have


# Task 2
browser.open_url("https://google.com/ncr")

search_box_input = browser.element(by.xpath("//textarea[@name='q']")).should(be.blank)
search_box_input.type('funny dogs').press_enter()

result_links = browser.all(by.xpath('//*[@id="rso"]//a/h3'))
assert len(result_links) == 9, f'Less then 9 result links present'
