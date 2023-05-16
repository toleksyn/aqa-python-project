# - Open http://rozetka.com.ua home page
# - Click on the user icon in the top right corner
# - Verify that the login modal is displayed
# - Close the login modal, verify it’s closed

from selene import browser, by, be, have, config

# Task 2
# arrange
config.timeout = 10
browser.open_url('https://rozetka.com.ua/ua/')
# act
browser.element(by.xpath("//header/div/div/ul/li[3]/rz-user/button")).click()
# assert
browser.element(by.xpath('//*[@id="auth_email"]')).should(be.visible)
browser.element(by.xpath('//*[@id="auth_pass"]')).should(be.visible)
browser.element(by.xpath("//div[@class='form__row auth-modal__form-bottom']/button[1]")).should(be.clickable)

browser.element(by.xpath("//rz-single-modal-window/div[3]/div[1]/button")).click()

browser.element(by.xpath("//input[@name='search']")).should(be.visible)
browser.element(by.xpath("//app-slider/div/button[1]")).should(be.clickable)
browser.element(by.xpath("//app-slider/div/button[2]")).should(be.clickable)
browser.element(by.xpath("//rz-top-slider/ul/li/a")).should(have.text("Всі акції"))


