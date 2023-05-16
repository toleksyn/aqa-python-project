# - Open http://rozetka.com.ua home page
# - Search for ‘dell’
# - Verify that at least 10 result links are displayed
# - Save the name and the price of 5th product, add it to the basket
# - Verify the basket modal is opened and the price and name are correct
from selene import browser, by, be, have


# Task 3
# arrange
browser.open_url('https://rozetka.com.ua/ua/')
# act
search_field = browser.element(by.xpath("//input[@name='search']")).should(be.visible)
search_field.type("dell").press_enter()
# assert
browser.all(by.xpath("//a/span[contains(text(), 'Dell')]")).should(have.size_at_least(10))

fifth_element_price = browser.element(by.xpath("//rz-grid/ul/li[5]/rz-catalog-tile"
                                               "/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span")).text
fifth_element_name = browser.element(by.xpath("//rz-grid/ul/li[5]/rz-catalog-tile"
                                              "/app-goods-tile-default/div/div[2]/a[2]/span")).text

browser.element(by.xpath("//rz-grid/ul/li[5]/rz-catalog-tile"
                         "/app-goods-tile-default/div/div[2]/div[4]/div[2]/app-buy-button/button")).click()
browser.element(by.xpath("//rz-cart/button")).click()

fifth_element_name_in_basket = browser.element(by.xpath("//rz-cart-product/div/div[1]/div/a")).text
fifth_element_price_in_basket = browser.element(by.xpath('//p[@class="cart-product__price cart-product__price--red"]')).text

assert fifth_element_name == fifth_element_name_in_basket and fifth_element_price == fifth_element_price_in_basket
