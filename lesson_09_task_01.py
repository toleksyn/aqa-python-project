from selene import browser, by, be, have


browser.open('https://rozetka.com.ua/')
browser.element(by.name('search')).type('iPhone').press_enter()
browser.all(by.xpath("//a/span[contains(text(), 'iPhone')]")).should(have.size_greater_than_or_equal(5))
#third_product_price = browser.all(by.xpath('//span[@class="goods-tile__price-value"]'))[3].should(be.present)
third_product = browser.all(by.xpath('//div[@class="goods-tile__inner"]//a[contains(., "iPhone")]'))[3].click()
