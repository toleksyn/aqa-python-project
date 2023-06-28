from selene import browser, by, be, query

class IherbCheckoutPage:

    def get_product_name(self, product_number):
        browser.element(by.xpath("//*[name()='svg' and @class='LandingPanel__ToggleIcon-sc-bh59r1-4 fUUZvX']"))\
            .wait.for_(be.visible)
        browser.element(by.xpath("//*[name()='svg' and @class='LandingPanel__ToggleIcon-sc-bh59r1-4 fUUZvX']"))\
            .click()
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