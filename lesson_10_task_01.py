from selene import browser, by, have, be
from selene.support.shared import config
from should import should


#from rozetka_home_page import RozetkaHomePage
#from rozetka_search_result_page import RozetkaSearchResultPage
#from rozetka_product_page import RozetkaProductPage

class RozetkaHomePage:
    def open(self):
        browser.open('https://rozetka.com.ua/')

    def search(self, keyword):
        browser.element(by.name('search')).type(keyword).press_enter()

        return RozetkaSearchResultPage()

    def open_login_form(self):
        browser.element('(//button[@class="header__button ng-star-inserted"])[1]')

class RozetkaSearchResultPage:

    def verify_search_results_at_least(self, number_of_results):
        browser.all(by.xpath("//a/span[contains(text(), 'iPhone')]")) \
            .should(have.size_greater_than_or_equal(number_of_results)) \
 \

    def verify_the_3rd_product_price(self, number_of_results):
        browser.all(by.xpath('//span[@class="goods-tile__price-value"]') \
                             .should, be.visible) \
 \
 \
class RozetkaProductPage:
    def product_page_link(self, number_of_results):
        browser.element(by.xpath('//div[@class="goods-tile__inner"]//a[contains(., "iPhone")]'))
        .should(be.clickable).click()

    def open_product_page(self):
        product_page = browser.element(by.xpath('//div[@class="goods-tile__inner"]//a[contains(., "iPhone")]'))
        product_page.should(be.clickable).click()

        # line 14, in open_product_page
        # product_page = browser.element(by.xpath('//div[@class="goods-tile__inner"]//a[contains(., "iPhone")]'))[3]
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
        # TypeError: 'Element' object is not subscriptable

    def get_product_price(self):
        browser.element(by.xpath('//p[@class="product-price__big product-price__big-color-red"]'))

def test_rozetka_search():
    config.timeout = 40

    rozetka_home_page = RozetkaHomePage()
    rozetka_home_page.open()
    search_result_page = rozetka_home_page.search("iphone")
    search_result_page.verify_search_results_at_least(5)
    search_result_page.verify_the_3rd_product_price(3)
    product_page = RozetkaProductPage()
    product_page.open_product_page(3)



test_rozetka_search()
