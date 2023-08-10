from appium import webdriver
from pages.mobile_page_objects.preferences_screen import PreferencesScreen

appium_options = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Pixel 6 PRO API 30',
    'appPackage': 'com.iherb',
    'appActivity': '.mobile.product.splash.view.SplashActivity'
}

appium_server_url = 'http://localhost:4723/wd/hub'
appium_driver = webdriver.Remote(appium_server_url, appium_options)
appium_driver.implicitly_wait(25)

home_screen = PreferencesScreen().save_preferences()
search_results_screen = home_screen.search('vitamin d')
filter_name = 'NOW Foods'
select_brand = search_results_screen.open_filter_and_sort_drawer()
select_brand.set_filter(filter_name)
the_first_product_name = search_results_screen.get_product_name(1)
the_fourth_product_name = search_results_screen.get_product_name(4)
assert the_first_product_name.startswith(filter_name), f"Product title doesn't contain {filter_name}"
assert the_fourth_product_name.startswith(filter_name), f"Product title doesn't contain {filter_name}"
