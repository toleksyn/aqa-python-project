from selene import browser, by, be, have
from selene.support.jquery_style_selectors import s
from selene import config

# Open Google home page
browser.open_url("https://google.com/ncr")

# Search for 'Selene'
search_input = s("//textarea[@id='APjFqb']")
search_input.type('Selene').press_enter()

# Verify that the first link contains Selene in its text
browser.all("//div[@id='rso']")[0].element(by.xpath('.//h3')).should(have.text('Selene'))

# Verify that you navigated back to the home page and that homepage is open
browser.element(by.xpath("//*[@id='logo']/img")).click()
browser.element(by.xpath("//*[@id='APjFqb']")).click()
browser.element(by.xpath('//form/div[1]/div[1]/div[4]/center/input[1]')).click()
browser.element(by.xpath('//form/div[1]/div[1]/div[4]/center/input[2]')).click()
