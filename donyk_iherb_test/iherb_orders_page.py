from selene import browser, by, be

class OrdersPage:

    def verify_order_number_is_displayed(self):
        browser.element(by.xpath('//div[@class="order-info-span rtl"]/span[2])[1]')).should(be.visible)
