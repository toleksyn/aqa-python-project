from selene import browser, by, be, have


# Task 3
browser.open_url("https://google.com")

search_box_input = browser.element(by.xpath("//textarea[@name='q']")).should(be.blank)
search_box_input.type('Selene').press_enter()

browser.all("//div[@id='rso']")[0].element(by.xpath('.//h3')).should(have.text('Selene'))

browser.element(by.xpath("//*[@id='logo']/img")).click()
browser.element(by.xpath("//img[@alt='Google']")).should(be.visible)
browser.element(by.xpath("//input[@class='gNO89b']")).should(be.clickable)
browser.element(by.xpath("//input[@class='RNmpXc']")).should(be.clickable)
