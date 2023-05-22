# "- Open http://rozetka.com.ua home page
# - Search for ‘iPhone’
# - Verify that at least 5 result links are displayed and that each link text contains 'iPhone'
# - Verify the 3rd product has a price, save the price
# - Click on the 3rd product and verify that the stored price and price on product page is equal
from selene import browser, by, be, have


# Task 1
# arrange
browser.open_url('https://rozetka.com.ua/ua/')
# act
search_field = browser.element(by.xpath("//input[@name='search']")).should(be.visible)
search_field.type("iPhone").press_enter()

# assert
browser.all(by.xpath("//a/span[contains(text(), 'iPhone')]")).should(have.size_at_least(5))
third_element_price = browser.element(by.xpath("(//span[@class='goods-tile__price-value'])[3]")).text

browser.element(by.xpath("(//span[@class='goods-tile__title'])[3]")).click()

third_element_price_on_pdp = \
    browser.element(by.xpath("//p[@class='product-price__big product-price__big-color-red']")).text

assert third_element_price == third_element_price_on_pdp
