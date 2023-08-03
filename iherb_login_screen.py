from appium.webdriver.common.appiumby import AppiumBy
from iherb_register_form_screen import IherbSignFormScreen

class IherbLoginScreen:
    def __init__(self, driver):
        self.driver = driver

    def tap_sign_in_button(self) -> IherbSignFormScreen:
        sign_in_button = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Sign up / Sign in']")
        sign_in_button.click()
        return IherbSignFormScreen(self.driver)