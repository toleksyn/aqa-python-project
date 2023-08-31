# Open iherb home page
# Search for ‘vitamin e’
# Verify at least 5 products are displayed
# Save the name of 5th product, add it to the cart
# Verify it’s added.
# Proceed to the checkout page.
# Verify the product name on checkout page is the same as in step 4.
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
my_account_page = homepage.open_my_account()

login_landing_page = my_account_page.open_login_landing_page()
create_an_account_page = login_landing_page.open_create_an_account_page()
returning_customer_page = create_an_account_page.open_returning_customers_page()
notifications_popup = returning_customer_page.log_in_with_iherb_account('roman.omelchenko@external.iherb.com', 'Qwertyuio?')

my_account_page = notifications_popup.close_popup()
homepage = my_account_page.open_home_page()

search_results_page = homepage.search('vitamin e')
search_results_page.verify_that_search_results_have_size_at_least(5)

product_number = 1
product_name = search_results_page.get_product_name(product_number)
added_to_cart_popup = search_results_page.add_to_cart(product_number)

cart_page = added_to_cart_popup.open_cart_page()
checkout_options_drawer = cart_page.open_checkout_options_drawer()

checkout_page = checkout_options_drawer.open_checkout_page()

checkout_items_page = checkout_page.open_checkout_cart_page()
checkout_product_name = checkout_items_page.get_full_product_name(product_number)

assert product_name == checkout_product_name, f'Product names are not equal'

driver.quit()
