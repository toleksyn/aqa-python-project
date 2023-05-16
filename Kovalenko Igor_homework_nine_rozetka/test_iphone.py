from selene import browser, by, be, have
from selene.support.jquery_style_selectors import s
import pytest

# Open Rozetka home page
browser.driver().get('https://rozetka.com.ua/')

# Search for ‘iPhone’
search_field = browser.element(by.xpath('//input[@name="search"]'))
search_field.should(be.clickable).type("iPhone").press_enter()

# Wait for the search results to load
browser.all(by.xpath('//ul[@class="catalog-grid ng-star-inserted"]')).should(have.size_greater_than_or_equal(0))

# Verify that at least 5 result links are displayed and that each link text contains 'iPhone'
results = browser.all('//a/span[contains(text(), "iPhone")]').should(have.size_greater_than_or_equal(5))

# Verify the 3rd product has a price, save the price
third_product = browser.element(by.xpath('//rz-grid/ul/li[3]'))
price_plp = browser.element(by.xpath('//rz-grid/ul/li[3]/rz-catalog-tile/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span')).text

# Click on the 3rd product and verify that the stored price and price on product page is equal
third_product.should(be.clickable).click()
price_pdp = browser.element(by.xpath('//p[@class="product-price__big product-price__big-color-red"]')).text

assert price_plp == price_pdp, f'The stored price and price on product page is not equal'

