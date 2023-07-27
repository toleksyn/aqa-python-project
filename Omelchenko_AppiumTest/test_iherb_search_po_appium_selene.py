from appium import webdriver
from selene import browser
from Omelchenko_AppiumTest.AppiumSelenePageObjectClasses.currency_language_page_selene import CurrencyLanguagePage


appium_options = dict(
    platformName="Android",
    automationName="uiautomator2",
    deviceName="Pixel 4a API 32",
    appPackage="com.iherb",
    appActivity=".mobile.product.splash.view.SplashActivity",
    NoReset="true"
)
appium_server_url = 'http://localhost:4723/wd/hub'
browser.config.driver = webdriver.Remote(appium_server_url, appium_options)
browser.config.timeout = 15

homepage = CurrencyLanguagePage().save_preferences()
search_results_page = homepage.search('vitamin a')

product_number = 1
product_price = search_results_page.get_product_price(product_number)
product_details_page = search_results_page.open_product_details_page(product_number)
product_details_price = product_details_page.get_product_price()

assert product_price == product_details_price, f'Prices are not equal'
browser.quit()
