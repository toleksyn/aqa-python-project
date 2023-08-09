from appium.webdriver.common.appiumby import AppiumBy

from iherb_login_screen import IherbLoginScreen

class IherbMyAccountScreen:
    def __init__(self, driver):
        self.driver = driver

    def open_login_landing_screen(self) -> IherbLoginScreen:
        sign_in_create_account_button = self.driver.find_element(AppiumBy.ID, "com.iherb:id/tv_sign_in")
        sign_in_create_account_button.click()
        return IherbLoginScreen(self.driver)

    def open_home_screen(self):
        homescreen_button = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/navigation_bar_item_icon_view']")
        homescreen_button.click()
        from iherb_home_screen import IherbHomeScreen
        return IherbHomeScreen(self.driver)