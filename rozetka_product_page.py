from selene import browser, by, be, query


class RozetkaProductPage:
    def get_price_from_pdp(self):
        price_element = browser.element(
            by.xpath('//p[@class="product-price__big product-price__big-color-red"]'))
        return price_element.get(query.text)
