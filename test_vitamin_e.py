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

home_screen = IherbCurrencyLanguageScreen(appium_driver).save_preferences()
my_account_screen = home_screen.open_my_account()

login_screen = my_account_screen.open_login_landing_screen()
login_form = login_screen.tap_sign_in_button()
returning_customers_screen = login_form.open_returning_customers_screen()
notifications_popup = returning_customers_screen.log_in_with_iherb_account('auto-tests@yopmail.com', 'Test1234!')

my_account_screen = notifications_popup.close_popup()
home_screen = my_account_screen.open_home_screen()

search_results_screen = home_screen.search('vitamin e')
search_results_screen.verify_that_search_results_have_size_at_least(3)

product_number = 1
product_name = search_results_screen.get_product_name(product_number)
added_to_cart_popup = search_results_screen.add_to_cart(product_number)

cart_screen = added_to_cart_popup.open_cart_screen()
checkout_options_drawer = cart_screen.open_checkout_options_drawer()

checkout_screen = checkout_options_drawer.open_checkout_screen()

checkout_items_screen = checkout_screen.open_checkout_cart_screen()
checkout_product_name = checkout_items_screen.get_full_product_name(product_number)

assert product_name == checkout_product_name, f'Product names are not equal'

appium_driver.quit()