from appium.webdriver.common.appiumby import AppiumBy

class IherbRerurningCustomerScreen:
    def __init__(self, driver):
        self.driver = driver

    def sign_in_with_credentials(self, username, password):
        username_input = self.driver.find_element(AppiumBy.XPATH, "//*[@hint='Your iHerb Mobile Number or Email']")
        self.driver.find_element(AppiumBy.XPATH, "//*[@hint='Your iHerb Mobile Number or Email']").click()
        username_input.send_keys(username)
        password_input = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='Password']")
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='Password']").click()
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
        sign_in_button.click()
        from iherb_home_screen import IherbHomeScreen
        return IherbHomeScreen(self.driver)

    def get_error_message_text(self):
        error_message = self.driver.find_element(AppiumBy.XPATH, "//*[@bounds='[126,398][786,444]']")
        return error_message.text