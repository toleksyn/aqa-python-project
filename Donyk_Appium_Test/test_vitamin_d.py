from appium import webdriver
from Donyk_Appium_Test.currency_language_screen import CurrencyLanguageScreen


appium_options = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='R28M32H8XGM',
    appPackage='com.iherb',
    appActivity='.mobile.product.splash.view.SplashActivity',
    NoReset='true'
)

appium_server_url = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(appium_server_url, appium_options)
driver.implicitly_wait(30)

home_screen = CurrencyLanguageScreen(driver).save_preferences()
search_results_screen = home_screen.search('vitamin d')

filter_name = 'NOW Foods'
select_brand = search_results_screen.open_filter_and_sort_drawer()
select_brand.set_brands_filter(filter_name)

first_product_name = search_results_screen.get_product_name(1)
second_product_name = search_results_screen.get_product_name(2)
third_product_name = search_results_screen.get_product_name(3)

assert first_product_name.startswith(filter_name), f"Product doesn't contain {filter_name} in the name"
assert second_product_name.startswith(filter_name), f"Product doesn't contain {filter_name} in the name"
assert third_product_name.startswith(filter_name), f"Product doesn't contain {filter_name} in the name"
driver.quit()
