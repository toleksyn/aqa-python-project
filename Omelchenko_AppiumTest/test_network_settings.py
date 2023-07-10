from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

appium_options = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 4a API 32',
    appPackage='com.android.settings',
    appActivity='.Settings'
)

appium_server_url = 'http://localhost:4723/wd/hub'
appium_driver = webdriver.Remote(appium_server_url, appium_options)
appium_driver.implicitly_wait(15)

network_element = appium_driver.find_element(AppiumBy.XPATH, '//*[@text="Network & internet"]')
network_element.click()
internet_element = appium_driver.find_element(AppiumBy.XPATH, '//*[@text="Internet"]')
internet_element.click()

expected_page_title = appium_driver.find_element(AppiumBy.XPATH, '//*[@content-desc="Internet"]')
assert expected_page_title.is_displayed()
appium_driver.quit()
