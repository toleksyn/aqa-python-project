from appium.webdriver.common.appiumby import AppiumBy


class NotificationsPopup:
    def __init__(self, driver):
        self.driver = driver

    def close_popup(self):
        not_now_button = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/tv_left']")
        not_now_button.click()
        from Omelchenko_AppiumTest.AppiumPageObjectClasses.my_account_page import MyAccountPage
        return MyAccountPage(self.driver)
