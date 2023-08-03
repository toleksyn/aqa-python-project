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
appium_driver.implicitly_wait(20)

home_screen = PreferencesScreen().save_preferences()
search_results_page = home_screen.search('vitamin a')

search_results_page.verify_search_results_at_least(3)

product_number = 3
product_price = search_results_page.get_product_price_from_search_serults(product_number)
product_details_page = search_results_page.open_product_details_screen(product_number)
product_details_price = product_details_page.get_product_price_from_product_details_screen()

assert product_price == product_details_price, f'Prices are not equal'
