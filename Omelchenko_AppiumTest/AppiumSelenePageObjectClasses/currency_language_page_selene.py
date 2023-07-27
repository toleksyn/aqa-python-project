from appium.webdriver.common.appiumby import AppiumBy
from selene import browser

from Omelchenko_AppiumTest.AppiumSelenePageObjectClasses.homepage_selene import HomePage


class CurrencyLanguagePage:
    def save_preferences(self) -> HomePage:
        save_country_preferences_button = browser.element((AppiumBy.XPATH, "//*[@text='Save']"))
        save_country_preferences_button.click()
        return HomePage()
