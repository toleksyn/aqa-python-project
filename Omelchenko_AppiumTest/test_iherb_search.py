from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

appium_options = dict(
    platformName="Android",
    automationName="uiautomator2",
    deviceName="Pixel 4a API 32",
    appPackage="com.iherb",
    appActivity=".mobile.product.splash.view.SplashActivity",
    NoReset="true"
)

appium_server_url = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(appium_server_url, appium_options)
driver.implicitly_wait(30)

save_country_preferences_button = driver.find_element(AppiumBy.XPATH, "//*[@text='Save']")
save_country_preferences_button.click()

search_field = driver.find_element(AppiumBy.XPATH, "//*[@text='Search iHerb']")
search_field.click()
search_box = driver.find_element(AppiumBy.XPATH, "//*[@text='Search iHerb']")
search_box.send_keys('vitamin a')
driver.execute_script('mobile: performEditorAction', {"action": "search"})

first_product_price = driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/discount_price'])[1]").text

product_card = driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/product_info_item'])[1]")
product_card.click()
product_price_on_pdp = driver.find_element(AppiumBy.ID, 'com.iherb:id/discounted_price').text

print(first_product_price, product_price_on_pdp)
assert first_product_price == product_price_on_pdp, f'Prices are not equal'
driver.quit()
