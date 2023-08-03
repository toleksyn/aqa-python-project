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
my_account_screen = home_screen.my_account_icon()
sign_in_sign_up_screen = my_account_screen.sign_in_button_1()
create_account_screen = sign_in_sign_up_screen.sign_in_button_2()
returning_customer_screen = create_account_screen.sign_in_button_3
returning_customer_screen.set_username("nonexisting@mail.com").set_password("nonexistingpassword").submit_the_login_form()
actual_error_text = returning_customer_screen.get_error_text()
expected_error_text = "Invalid email, phone number, or password"
assert actual_error_text == expected_error_text, f"The error texts are not matched"

