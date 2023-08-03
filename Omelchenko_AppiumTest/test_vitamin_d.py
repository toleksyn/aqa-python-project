# Open iherb home page
# Search for ‘vitamin d’
# Verify at least 5 products are displayed
# In the filter section, check the NOW Foods checkbox
# Verify the all displayed products have ‘NOW Foods’ in the name
from appium import webdriver
from Omelchenko_AppiumTest.AppiumPageObjectClasses.currency_language_page import CurrencyLanguagePage

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

homepage = CurrencyLanguagePage(driver).save_preferences()
search_results_page = homepage.search('vitamin d')
search_results_page.verify_that_search_results_have_size_at_least(5)

filter_and_sort_drawer = search_results_page.open_filter_and_sort_drawer()

filter_name = 'NOW Foods'
filter_and_sort_drawer.set_brands_filter(filter_name)

first_product_name = search_results_page.get_product_name(1)
second_product_name = search_results_page.get_product_name(2)
third_product_name = search_results_page.get_product_name(3)

assert first_product_name.startswith(filter_name), f'Product is not {filter_name} one'
assert second_product_name.startswith(filter_name), f'Product is not {filter_name} one'
assert third_product_name.startswith(filter_name), f'Product is not {filter_name} one'

driver.quit()

