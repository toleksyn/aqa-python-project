from selene import browser, by, be, have

# Task 3
browser.open_url('http://rozetka.com.ua')

# Search for 'Dell'
search_input = browser.element(by.xpath('//input[@name="search"]')).should(be.visible)
search_input.type('Dell').press_enter()

# Verify that at least 10 result links are displayed
browser.all(by.xpath('//a/span[contains(text(),"Dell")]')).should(have.size_at_least(10))

# Save the name and price of the 5th product, add it to the basket
fifth_product_name = browser.element(by.xpath('(//span[@class="goods-tile__title"])[5]')).text
fifth_product_price = browser.element(by.xpath('(//span[@class="goods-tile__price-value"])[5]')).text
add_to_basket_button = browser.element(by.xpath('(//button[@class="buy-button goods-tile__buy-button ng-star-inserted"])[5]')).click()

# Verify the basket modal is opened and the price and name are correct
basket_modal = browser.element(by.xpath('//button[@class="header__button ng-star-inserted header__button--active"]')).click()
added_product_name = browser.element(by.xpath('//a[@class="cart-product__title"]')).text
added_product_price = browser.element(by.xpath('//p[@class="cart-product__price"]')).text
assert added_product_name == fifth_product_name
assert added_product_price == fifth_product_price