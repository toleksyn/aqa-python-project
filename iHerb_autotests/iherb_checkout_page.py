from selene import browser, by, be, query

from iherbtestvenv.iherb_payment_update_page import IherbPaymentUpdatePage
from iherbtestvenv.iherb_thank_you_page import IherbThankYouPage

class IherbCheckoutPage:

    def get_product_name(self, product_number):
        product_name = browser.element(by.xpath("//*[name()='svg' and @class='LandingPanel__ToggleIcon-sc-bh59r1-4 fUUZvX']"))
        product_name.wait.for_(be.visible)
        product_name.click()
        return self.get_product_brand(product_number) + ', ' + self.get_product_display_name(product_number)

    def get_product_brand(self, product_number):
        product_brand = browser.element(by.xpath(
            "(//div[@class='List__ProductDetails-sc-1mvgpt5-17 gtRIby']/div[1])[{0}]".format(str(product_number))))
        product_brand.wait.for_(be.visible)
        return product_brand.get(query.text)

    def get_product_display_name(self, product_number):
        product_name = browser.element(by.xpath(
            "(//div[@class='List__ProductDetails-sc-1mvgpt5-17 gtRIby']/div[2])[{0}]".format(str(product_number))))
        product_name.wait.for_(be.visible)
        return product_name.get(query.text)

    def select_shipping_address(self, address_number):
        browser.element(by.xpath("(//div[@class='Item__AddressInfo-sc-38bdg3-6 gxdBoo'])[{0}]"
                                 .format((str(address_number))))).click()
        browser.element(by.xpath("//button[@data-testid='address-continue-button']")).click()
        return self

    def place_order_with_incorrect_card(self) -> IherbPaymentUpdatePage:
        browser.element(by.xpath("//*[@id='place-order-button']")).click()
        return IherbPaymentUpdatePage()

    def place_order_with_correct_card(self) -> IherbThankYouPage:
        browser.element(by.xpath("//*[@id='place-order-button']")).click()
        return IherbThankYouPage()
