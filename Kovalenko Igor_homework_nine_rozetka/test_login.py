from selene import browser, by, be, have
import pytest

# Open Rozetka home page
browser.driver().get('https://rozetka.com.ua/')

# Click on the user icon in the top right corner
browser.element(by.xpath('//button[@class="header__button ng-star-inserted"]')).click()

# Verify that the login modal is displayed
browser.element(by.xpath('//div[@class="modal__content"]')).should(be.visible)
browser.element(by.xpath('//input[@type="email"]')).should(be.clickable)
browser.element(by.xpath('//button[text()="Увійти"]'))
browser.element(by.xpath('//button[text()="Зареєструватися"]'))
browser.element(by.xpath('//app-slider/div/button[1]')).should(be.clickable)
browser.element(by.xpath('//app-slider/div/button[2]')).should(be.clickable)

# Close the login modal
browser.element(by.xpath('//button[@class="modal__close"]')).click()

# Verify that modal is closed
browser.element(by.xpath('//div[@class="modal__content"]')).should_not(be.visible)