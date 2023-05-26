from selene import browser, by, be, have

# Task 1
browser.open_url('http://rozetka.com.ua')

# Search for 'iPhone'
search_input = browser.element(by.xpath('//input[@name="search"]')).should(be.visible)
search_input.type('iPhone').press_enter()

# Verify that at least 5 result links are displayed and each link text contains 'iPhone'
browser.all(by.xpath('//a/span[contains(text(),"iPhone")]')).should(have.size_at_least(5))

# Verify the 3rd product has a price, save the price
third_product_price = browser.element(by.xpath('(//span[@class="goods-tile__price-value"])[3]')).text

# Click on the 3rd product and verify the stored price and price on product page is equal
browser.element(by.xpath('//div[@data-goods-id="352486566"]')).click()

product_page_price = browser.element(by.xpath('//p[@class="product-price__big product-price__big-color-red"]')).text
assert third_product_price == product_page_price
