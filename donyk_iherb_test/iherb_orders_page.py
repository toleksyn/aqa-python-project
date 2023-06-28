from selene import browser, by

class OrdersPage:

    def verify_order(self):
        return browser.element(by.xpath('//div[@class="order-info-span rtl"]')).text
