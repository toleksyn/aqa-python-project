from selene import browser, by, be, have
import pytest

# Open Rozetka home page
browser.driver().get('https://rozetka.com.ua/')

# Search for ‘Dell’
search_field = browser.element(by.xpath('//input[@name="search"]'))
search_field.should(be.clickable).type("Dell").press_enter()

# Verify that at least 10 result links are displayed
results = browser.all(by.xpath("//a/span[contains(text(), 'Dell')]")).should(have.size_at_least(10))

# Save the name and the price of 5th product, add it to the basket
fifth_product_name_on_search_page = browser.element(by.xpath("(//div[contains(@class,'goods-tile__inner')])[5]//a[contains(@class,'goods-tile__heading')]/span"))
fifth_product_price_on_search_page = browser.element(by.xpath("(//div[contains(@class,'goods-tile__inner')])[5]//span[contains(@class,'goods-tile__price-value')]"))

browser.element(by.xpath("(//div[@class='goods-tile__inner']//button[contains(@class, 'buy-button')])[5]")).click()

# Verify the basket modal is opened and the price and name are correct
browser.element(by.xpath('//button[@class="header__button ng-star-inserted header__button--active"]')).click()
browser.element(by.xpath('//h3[@class="modal__heading"]')).should(be.visible)
browser.element(by.xpath('//button[@class="modal__close"]')).should(be.clickable)
browser.element(by.xpath('//a[@class="cart-product__title"]')).should(be.visible)
browser.element(by.xpath('//p[@class="cart-product__price"]')).should(be.visible)
browser.element(by.xpath('//a[@data-testid="cart-receipt-submit-order"]')).should(be.clickable)

fifth_product_name_in_basket = browser.element(by.xpath('//a[@class="cart-product__title"]'))
fifth_product_price_in_basket = browser.element(by.xpath('//p[@class="cart-product__price"]'))

assert fifth_product_name_on_search_page.text == fifth_product_name_in_basket.text, f'Product`s name in Basket is incorrect'
assert fifth_product_price_on_search_page.text == fifth_product_price_in_basket.text, f'Product`s price in Basket is incorrect'
