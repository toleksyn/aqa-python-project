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
fifth_product_name = browser.element(by.xpath('//rz-grid/ul/li[5]/rz-catalog-tile/app-goods-tile-default/div/div[2]/a[2]/span')).text
fifth_product_price = browser.element(by.xpath('//rz-grid/ul/li[5]/rz-catalog-tile/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span')).text

browser.element(by.xpath('//rz-grid/ul/li[5]/rz-catalog-tile/app-goods-tile-default/div/div[2]/div[4]/div[2]/app-buy-button/button')).click()

# Verify the basket modal is opened and the price and name are correct
browser.element(by.xpath('//button[@class="header__button ng-star-inserted header__button--active"]')).click()
browser.element(by.xpath('//h3[@class="modal__heading"]')).should(be.visible)
browser.element(by.xpath('//button[@class="modal__close"]')).should(be.clickable)
browser.element(by.xpath('//rz-cart-product/div/div[1]/div/a')).should(be.visible)
browser.element(by.xpath('//p[@class="cart-product__price cart-product__price--red"]')).should(be.clickable)

fifth_product_name_basket = browser.element(by.xpath("//rz-cart-product/div/div[1]/div/a")).text
fifth_product_price_basket = browser.element(by.xpath('//p[@class="cart-product__price cart-product__price--red"]')).text

assert fifth_product_name == fifth_product_name_basket, f'Product`s name in Basket is incorrect'
assert fifth_product_price == fifth_product_price_basket, f'Product`s price in Basket is incorrect'

