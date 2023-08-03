from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
from selene.support.conditions import have


def appium_sample_test():
    appium_options = AppiumOptions()
    appium_options.new_command_timeout = 60
    appium_options.platform_name = 'android'
    appium_options.automation_name = 'uiautomator2'
    appium_options.set_capability('deviceName', 'Pixel_3a_API_34_extension_level_7_arm64-v8a')
    appium_options.set_capability('appPackage', 'com.android.settings')
    appium_options.set_capability('appActivity', '.Settings')
    appium_server_url = 'http://localhost:4723/wd/hub'

    browser.config.driver = webdriver.Remote(appium_server_url, appium_options)  # appium driver
    battery_element = browser.element((AppiumBy.XPATH, '//*[@text="Battery"]'))
    battery_element.wait.until(have.value('some'))
    battery_element.click()
    browser.element((AppiumBy.XPATH, '//*[@resource-id="android:id/summary"]')).should(be.visible)