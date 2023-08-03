from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from iherb_search_results_screen import IherbSearchResultsScreen
from iherb_login_screen import IherbLoginScreen

class IherbHomeScreen:
    def __init__(self, driver):
        self.driver = driver

    def search(self, search_keyword) -> IherbSearchResultsScreen:
        search_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Search iHerb']")
        search_field.click()
        search_box = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Search iHerb']")
        search_box.send_keys(search_keyword)
        # This needed to perform search action, because .sendKeyEvent doesn't work
        # self.driver.execute_script('mobile: performEditorAction', {"action": "search"})
        actions = TouchAction(self.driver)
        actions.press(x=991, y=2098, pressure=1000)
        actions.wait(600).release().perform()
        return IherbSearchResultsScreen(self.driver)

    def sign_in(self) -> IherbLoginScreen:
        sign_in_button = self.driver.find_element(AppiumBy.ID, "com.iherb:id/txt_login")
        sign_in_button.click()
        return IherbLoginScreen(self.driver)