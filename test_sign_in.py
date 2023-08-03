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
appium_driver.implicitly_wait(40)

home_screen = IherbCurrencyLanguageScreen(appium_driver).save_preferences()

login_screen = home_screen.sign_in()
login_form = login_screen.tap_sign_in_button().tap_sign_in_button()
login_with_incorrect_data = login_form.sign_in_with_credentials("test_data_incorrect@yopmail.com", "Test1234")

error_message = login_form.get_error_message_text()

assert error_message == 'Invalid email, phone number, or password', f'Error message does not match the required'

appium_driver.quit()