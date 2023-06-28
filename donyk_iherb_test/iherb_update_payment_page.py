from selene import browser, by


class UpdatePaymentPage:


    def open_orders_page(self):
        browser.element(by.xpath('//div[@class="css-kvi0m9"]')).click()
        return OrdersPage()
