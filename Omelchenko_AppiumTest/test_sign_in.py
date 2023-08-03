# Open iherb home page
# Click the ‘Sign In’ button
# Try to sign in with non-existing credentials
# Verify that the error message is displayed ‘Invalid email, phone number, or password’
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
my_account = homepage.open_my_account()

login_landing_page = my_account.open_login_landing_page()
create_an_account_page = login_landing_page.open_create_an_account_page()
returning_customer_page = create_an_account_page.open_returning_customers_page()
returning_customer_page.log_in_with_iherb_account('invalid_credentials@yopmail.com', 'invalid_pass')
actual_error_message = returning_customer_page.get_error_message_text()

expected_error_message = 'Invalid email, phone number, or password'
assert actual_error_message == expected_error_message, f'Error message does not match the required'

driver.quit()

