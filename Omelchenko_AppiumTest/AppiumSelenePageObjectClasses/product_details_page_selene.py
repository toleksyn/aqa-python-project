from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, query


class ProductDetailsPage:
    def get_product_price(self):
        return browser.element((AppiumBy.ID, 'com.iherb:id/discounted_price')).get(query.text)
