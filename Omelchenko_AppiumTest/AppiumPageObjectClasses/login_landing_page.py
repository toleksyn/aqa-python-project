from appium.webdriver.common.appiumby import AppiumBy

from Omelchenko_AppiumTest.AppiumPageObjectClasses.create_an_account_page import CreateAnAccountPage


class LoginLandingPage:
    def __init__(self, driver):
        self.driver = driver

    def open_create_an_account_page(self) -> CreateAnAccountPage:
        sign_in_create_account_button = self.driver.find_element\
            (AppiumBy.ID, "com.iherb:id/login_page_button_sign_in_with_email")
        sign_in_create_account_button.click()
        return CreateAnAccountPage(self.driver)
