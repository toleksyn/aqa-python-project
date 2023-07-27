from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, query

from Omelchenko_AppiumTest.AppiumSelenePageObjectClasses.product_details_page_selene import ProductDetailsPage


class SearchResultsPage:
    def get_product_price(self, product_number):
        return browser.element((AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/discount_price'])[{0}]"
                                        .format(str(product_number)))).get(query.text)

    def open_product_details_page(self, product_number) -> ProductDetailsPage:
        product_card = browser.element((AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/product_info_item'])[{0}]"
                                       .format(str(product_number))))
        product_card.click()
        return ProductDetailsPage()
