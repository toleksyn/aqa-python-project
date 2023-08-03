from appium.webdriver.common.appiumby import AppiumBy


class ReturningCustomerScreen:

    def __init__(self, driver):
        self.driver = driver

    def sign_in(self, username, password):
        self.set_username(username)
        self.set_password(password)
        sign_in_button = self.driver.find_element(AppiumBy.XPATH, '//*[@resource-id="sign_in_button"]')
        sign_in_button.click()
        from Donyk_Appium_Test.home_screen import HomeScreen
        return HomeScreen(self.driver)

    def set_username(self, username):
        username_field = self.driver.find_element(AppiumBy.XPATH, '//*[@bounds="[98,467][1351,558]"]')
        username_field.click()
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = self.driver.find_element(AppiumBy.XPATH, '//*[@resource-id="Password"]')
        password_field.click()
        password_field.send_keys(password)

    def get_error_message_text(self):
        return self.driver.find_element(AppiumBy.XPATH, '//*[@bounds="[56,429][1389,548]"]').text
