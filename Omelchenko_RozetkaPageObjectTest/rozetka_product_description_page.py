from selene import browser
from selene.support import by


class RozetkaProductDescriptionPage:

    def get_product_price(self):
        return browser.element(by.xpath("//p[@class='product-price__big product-price__big-color-red']")).text
