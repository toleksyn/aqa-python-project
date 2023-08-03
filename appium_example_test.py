from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

def appium_sample_test():
    appium_options = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Pixel_3a_API_34_extension_level_7_arm64-v8a',
        app='globalapp-debug.apk',
        # appPackage='com.iherb.mobile.product.newhome',
        # appActivity='.ShopActivity'
    )

    appium_server_url = 'http://localhost:4723/wd/hub'
    appium_driver = webdriver.Remote(appium_server_url, appium_options)
    appium_driver.implicitly_wait(10)
    battery_element = appium_driver.find_element(by=AppiumBy.ID, value='id')
    battery_element.click()
    assert appium_driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="android:id/summary"]').is_displayed()
    appium_driver.quit()