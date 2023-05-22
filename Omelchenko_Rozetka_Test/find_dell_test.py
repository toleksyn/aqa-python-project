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

fifth_element_price = browser.element(by.xpath("(//span[@class='goods-tile__price-value'])[5]")).text
fifth_element_name = browser.element(by.xpath("(//span[@class='goods-tile__title'])[5]")).text

add_product_to_cart = browser.element(by.xpath("(//app-buy-button/button)[5]")).click()
click_cart_button_in_header = browser.element(by.xpath("//rz-cart/button")).click()

fifth_element_name_in_basket = browser.element(by.xpath("//div[@class='cart-product__main']/a")).text
fifth_element_price_in_basket = browser.element(by.xpath("//p[@class='cart-product__price']")).text

assert fifth_element_name == fifth_element_name_in_basket and fifth_element_price == fifth_element_price_in_basket
