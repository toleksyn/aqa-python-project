from appium.webdriver.common.appiumby import AppiumBy

from Omelchenko_AppiumTest.AppiumPageObjectClasses.notifications_popup import NotificationsPopup


class ReturningCustomersPage:
    def __init__(self, driver):
        self.driver = driver

    def log_in_with_iherb_account(self, username, password) -> NotificationsPopup:
        self.log_in(username, password)
        return NotificationsPopup(self.driver)

    def log_in(self, username, password):
        self.set_username(username)
        self.set_password(password)
        login_button = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='sign_in_button']")
        login_button.click()
        return self.driver

    def set_username(self, username):
        username_field = self.driver.find_element(AppiumBy.XPATH, "//*[@bounds='[77,391][1009,463]']")
        username_field.click()
        username_field.send_keys(username)
        return self.driver

    def set_password(self, password):
        password_field = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='Password']")
        password_field.click()
        password_field.send_keys(password)
        return self

    def get_error_message_text(self):
        return self.driver.find_element(AppiumBy.XPATH, "//*[@bounds='[126,389][786,435]']").text
