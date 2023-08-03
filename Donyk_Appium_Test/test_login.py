from appium import webdriver
from Donyk_Appium_Test.currency_language_screen import CurrencyLanguageScreen
from Donyk_Appium_Test import my_account_screen


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
my_account_screen = home_screen.open_my_account_screen()

login_screen = my_account_screen.open_login_screen()
create_an_account_screen = login_screen.open_create_an_account_screen()
returning_customer_screen = create_an_account_screen.open_returning_customer_screen()
returning_customer_screen.sign_in('test@yopmail.co', 'qwertyui')
error_message = returning_customer_screen.get_error_message_text()

expected_error = 'Invalid email, phone number, or password'
assert error_message == expected_error, f'Error message is different'
driver.quit()
