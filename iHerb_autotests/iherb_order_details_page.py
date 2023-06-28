from selene import browser, by, query

class IherbOrderDetailsPage:

    def verify_order_number(self, order_number):
        return browser.element(by.xpath("//span[contains(text(),'')][{0}]"
                                        .format(str(order_number)))).get(query.text)