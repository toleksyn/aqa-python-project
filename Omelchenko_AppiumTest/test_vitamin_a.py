# Open iherb home page
# Search for ‘vitamin a’
# Verify at least 5 products are displayed
# Save the reviews count for 5th product and click on it
# Verify the reviews count on product page is the same as in the previous step
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
search_results_page = homepage.search('vitamin a')
search_results_page.verify_that_search_results_have_size_at_least(5)

product_number = 3
product_review_amount = search_results_page.get_product_review_amount(product_number)
product_details_page = search_results_page.open_product_details_page(product_number)
product_details_review_amount = product_details_page.get_product_review_amount()

assert product_review_amount == product_details_review_amount, f'Prices are not equal'

driver.quit()
