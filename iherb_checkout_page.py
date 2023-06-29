from selene import browser, by, query
from pages.iherb_cart_page import IherbCartPage

class IherbCheckoutPage:
    def get_product_name(self):
        browser.all(f'(//div[@class="List__DisplayName-sc-1mvgpt5-4 djMfWv"]').get(query.text)
        return self

    def re_enter_credit_card_number(self, cart_number):
        browser.element(by.xpath('//input[@id="encryptedCardNumber"]')).type(cart_number)
        return IherbCartPage()

    def approve_credit_card_number(self):
        continue_button = browser.element(by.xpath('//button[@id="credit-card-continue-button"]')).click
        return IherbCartPage()

    def place_oredr(self):
        place_oredr_button = browser.element(by.xpath('//button[@id="place-order-button"]')).click
