from selene import browser, by, be, have

browser.open('https://rozetka.com.ua/')
user_icon = browser.element(by.xpath('//button[@class="header__button ng-star-inserted"]'))
user_icon.click()
email_input = browser.element(by.xpath('//input[@id="auth_email"]')).should(be.enabled)
password_input = browser.element(by.xpath('//input[@id="auth_pass"]')).should(be.enabled)
button_login = browser.element(by.xpath('//button[contains(text(),"Увійти")]')).should(be.enabled)
close_icon = browser.element(by.xpath('//button[@class="modal__close"]'))
close_icon.click()
email_input.should(be.disabled)
password_input.should(be.disabled)
button_login.should(be.disabled)
