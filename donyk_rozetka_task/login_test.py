from selene import browser, by, be, have

# Task 2
browser.open_url('http://rozetka.com.ua')

# Click on the user icon in the top right corner
browser.element(by.xpath('//button[@class="header__button ng-star-inserted"]')).click()

# Verify that the login modal is displayed
browser.element(by.xpath('//div[@class="modal__content"]')).should(be.visible)
browser.element(by.xpath('//input[@id="auth_email"]')).should(be.visible)
browser.element(by.xpath('//input[@id="auth_pass"]')).should(be.visible)
browser.element(by.xpath('//button[@class="button button--large button--green auth-modal__submit ng-star-inserted"]')).should(be.clickable)

# Close the login modal and verify it's closed
browser.element(by.xpath('//button[@class="modal__close"]')).click()
browser.element(by.xpath('//div[@class="modal__content"]')).should_not(be.visible)
