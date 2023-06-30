from selene import browser, by, be

from Omelchenko_iHerbTest.iherb_cart_page import IherbCartPage


class IherbCartModal:

    def open_cart_page(self) -> IherbCartPage:
        browser.element(by.xpath("//div[@class='checkout-button']")).click()
        return IherbCartPage()
