from selene import browser, by, be


class IherbCheckoutPage:

    def get_product_name(self, product_number):
        browser.element(by.xpath("//*[name()='svg' and @class='LandingPanel__ToggleIcon-sc-bh59r1-4 fUUZvX']")) \
            .assure(be.existing, timeout=15).click()
        return self.get_product_brand(product_number) + ', ' + self.get_product_display_name(product_number)

    def get_product_display_name(self, product_number):
        return browser.element(by.xpath("(//div[@class='List__ProductDetails-sc-1mvgpt5-17 gtRIby']/div[2])[{0}]"
                                        .format(str(product_number)))).text

    def get_product_brand(self, product_number):
        return browser.element(by.xpath("(//div[@class='List__ProductDetails-sc-1mvgpt5-17 gtRIby']/div[1])[{0}]"
                                        .format(str(product_number)))).text

    def select_shipping_address(self, address_number):
        browser.element(by.xpath("(//div[@class='Item__AddressInfo-sc-38bdg3-6 gxdBoo'])[{0}]"
                                 .format((str(address_number))))).click()
        browser.element(by.xpath("//button[@data-testid='address-continue-button']")).click()
        return self