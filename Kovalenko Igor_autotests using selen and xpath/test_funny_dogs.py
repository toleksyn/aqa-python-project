from selene import browser
from selene.support import by
from selene.support.jquery_style_selectors import s
from time import sleep

# open google home page
browser.open_url('https://www.google.com/')

# search for 'funny dogs'
search_input = s("//textarea[@id='APjFqb']")
search_input.type('funny dogs').press_enter()

# wait for search results to load
browser.element(by.xpath('//*[@id="rso"]/div[1]/div[1]/div[1]/a'))
sleep(5)

# get search result links
result_links = browser.all(by.xpath('//*[@id="rso"]//a/h3'))
assert len(result_links) == 9, f'Less than 9 result links are found'

# close the browser
browser.quit()
