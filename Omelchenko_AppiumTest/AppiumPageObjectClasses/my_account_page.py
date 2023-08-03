from appium.webdriver.common.appiumby import AppiumBy

from Omelchenko_AppiumTest.AppiumPageObjectClasses.login_landing_page import LoginLandingPage


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_landing_page(self) -> LoginLandingPage:
        sign_in_create_account_button = self.driver.find_element(AppiumBy.ID, "com.iherb:id/tv_sign_in")
        sign_in_create_account_button.click()
        return LoginLandingPage(self.driver)

    def open_home_page(self):
        homepage_button = self.driver.find_element(AppiumBy.XPATH, "//*[@bounds='[102,2186][168,2252]']")
        homepage_button.click()
        from Omelchenko_AppiumTest.AppiumPageObjectClasses.homepage import HomePage
        return HomePage(self.driver)
