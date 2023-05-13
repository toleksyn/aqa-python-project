from selene import browser
from selene.support import by

# Open Google home page
browser.open_url('https://www.google.com/')

# Search for 'funny kitten'
search_input = browser.element(by.xpath("//textarea[@id='APjFqb']"))
search_input.type('funny kitten').press_enter()

# Verify that first result link contains 'kitten' in its text
assert 'kitten' in browser.all("//div[@id='rso']")[0]\
                    .element(by.xpath('.//h3')).text.lower()
