from selene import browser, by, be

from Omelchenko_iHerbTest.iherb_order_details_page import IherbOrderDetailsPage


class IherbUpdatePaymentPage:

    def open_order_details_page(self) -> IherbOrderDetailsPage:
        browser.element(by.xpath("//div[@class='css-kvi0m9']//*[name()='svg']")).wait.for_(be.visible)
        browser.element(by.xpath("//div[@class='css-kvi0m9']//*[name()='svg']")).click()
        return IherbOrderDetailsPage()
