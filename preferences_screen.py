from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile_page_objects.home_page_screen import HomePageScreen

appium_options = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Pixel 6 PRO API 30',
    'appPackage': 'com.iherb',
    'appActivity': '.mobile.product.splash.view.SplashActivity'
}

appium_server_url = 'http://localhost:4723/wd/hub'
appium_driver = webdriver.Remote(appium_server_url, appium_options)
appium_driver.implicitly_wait(15)

class PreferencesScreen:
    def __init__(self):
        pass

    def save_preferences(self) -> HomePageScreen:
        save_country_preferences_button = appium_driver.find_element(AppiumBy.XPATH, "//*[@text='Save']")
        save_country_preferences_button.click()
        return HomePageScreen()