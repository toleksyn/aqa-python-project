from appium import webdriver
from iherb_currency_language_screen import IherbCurrencyLanguageScreen

appium_options = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Pixel 5 API 31',
        appPackage='com.iherb',
        appActivity='.mobile.product.splash.view.SplashActivity',
        NoReset = 'true'
    )

appium_server_url = 'http://localhost:4723/wd/hub'
appium_driver = webdriver.Remote(appium_server_url, appium_options)
appium_driver.implicitly_wait(30)

homescreen = IherbCurrencyLanguageScreen(appium_driver).save_preferences()
search_results_screen = homescreen.search('vitamin d')
search_results_screen.verify_that_search_results_have_size_at_least(3)

filter_and_sort_drawer = search_results_screen.open_filter_and_sort_drawer()

filter_name = 'NOW Foods'
filter_and_sort_drawer.set_brands_filter(filter_name)

first_product_name = search_results_screen.get_product_name(1)
second_product_name = search_results_screen.get_product_name(2)
third_product_name = search_results_screen.get_product_name(3)

assert first_product_name.startswith(filter_name), f"The product has no {filter_name} name"
assert second_product_name.startswith(filter_name), f"The product has no {filter_name} name"
assert third_product_name.startswith(filter_name), f"The product has no {filter_name} name"

appium_driver.quit()