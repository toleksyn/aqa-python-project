from selene import browser, by, be


class RozetkaProductPage:
    def get_price_from_pdp(self):
        browser.element(by.xpath('//p[@class="product-price__big product-price__big-color-red"]'))\
            .should(be.visible)
