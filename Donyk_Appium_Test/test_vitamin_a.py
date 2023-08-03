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
search_results_screen = home_screen.search('vitamin a')

product_number = 3
product_reviews_count = search_results_screen.get_product_reviews_count(product_number)
product_screen = search_results_screen.open_product_screen(product_number)
product_screen_reviews_count = product_screen.get_product_reviews_count()

assert product_reviews_count == product_screen_reviews_count, f'Product reviews count are different'
driver.quit()
