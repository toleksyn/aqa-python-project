from appium.webdriver.common.appiumby import AppiumBy
from Omelchenko_AppiumTest.AppiumPageObjectClasses.homepage_appium import HomePage


class CurrencyLanguagePage:

    def __init__(self, driver):
        self.driver = driver

    def save_preferences(self) -> HomePage:
        save_country_preferences_button = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Save']")
        save_country_preferences_button.click()
        return HomePage(self.driver)
