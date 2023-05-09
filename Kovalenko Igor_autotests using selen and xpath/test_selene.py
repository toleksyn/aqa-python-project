from selene import browser
from selene.support import by
from selene.support.jquery_style_selectors import s
from time import sleep

# Open Google home page
browser.open_url('https://www.google.com/')

# Search for 'Selene'
search_input = s("//textarea[@id='APjFqb']")
search_input.type('Selene').press_enter()

# Verify that the first link contains Selene in its text
first_result_link = browser.element('//*[@id="rso"]/div[1]/div/div')
assert 'Selene' in first_result_link.text, f"Expected 'Selene' to be in the first result link, but found '{first_result_link.text}'"

# Wait for 5 seconds for the search results to load
sleep(5)

# Click on Google logo on the search results page
google_logo = browser.element(by.xpath('//*[@id="logo"]/img'))
google_logo.click()

# Wait for 5 seconds for the search results to load
sleep(5)

# Verify that you navigated back to the home page and that home page is open
assert "Google" in browser.title(), f"Expected 'Google' to be in the title, but found '{browser.title()}'"