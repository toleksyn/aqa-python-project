from appium.webdriver.common.appiumby import AppiumBy

class IherbNotificationsPopup:
    def __init__(self, driver):
        self.driver = driver

    def close_popup(self):
        not_now_button = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/tv_left']")
        not_now_button.click()
        from iherb_my_account_screen import IherbMyAccountScreen
        return IherbMyAccountScreen(self.driver)