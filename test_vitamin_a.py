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
search_results_screen = homescreen.search('vitamin a')
search_results_screen.verify_that_search_results_have_size_at_least(3)

product_number = 3
third_product_review_on_search_screen = search_results_screen.get_product_review_amount(product_number)
third_product_details_screen = search_results_screen.open_product_details_page(product_number)
product_review_on_details_screen = third_product_details_screen.get_product_review_amount()

assert third_product_review_on_search_screen == product_review_on_details_screen, f"The stored review and review on " \
                                                                                    f"product page is not equal"
appium_driver.quit()