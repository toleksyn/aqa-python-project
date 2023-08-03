from appium.webdriver.common.appiumby import AppiumBy
from Donyk_Appium_Test.home_screen import HomeScreen


class CurrencyLanguageScreen:

    def __init__(self, driver):
        self.driver = driver

    def save_preferences(self):
        save_country_preferences = self.driver.find_element(AppiumBy.XPATH, '//*[@text="Save"]')
        save_country_preferences.click()
        return HomeScreen(self.driver)
