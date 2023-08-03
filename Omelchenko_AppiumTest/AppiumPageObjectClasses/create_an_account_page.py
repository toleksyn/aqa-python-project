from appium.webdriver.common.appiumby import AppiumBy

from Omelchenko_AppiumTest.AppiumPageObjectClasses.returning_customers_page import ReturningCustomersPage


class CreateAnAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def open_returning_customers_page(self) -> ReturningCustomersPage:
        sign_in_create_account_button = self.driver.find_element(AppiumBy.XPATH, "//*[@text=' Sign in']")
        sign_in_create_account_button.click()
        return ReturningCustomersPage(self.driver)
