from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile_page_objects.preferences_screen import appium_driver
from pages.mobile_page_objects.search_results_screen import SearchResultsScreen
from pages.mobile_page_objects.my_account_screen import MyAccountScreen

class HomePageScreen:
    def __init__(self, driver):
        self.driver = driver

    def search(self, search_keyword) -> SearchResultsScreen:
        search_field = appium_driver.find_element(AppiumBy.XPATH, "//*[@text='Search iHerb']")
        search_field.click()
        search_box = appium_driver.find_element(AppiumBy.XPATH, "//*[@text='Search iHerb']")
        search_box.send_keys(search_keyword)
        appium_driver.execute_script('mobile: performEditorAction', {"action": "search"})
        return SearchResultsScreen()

    def open_my_account_screen(self):
        appium_driver.find_element(AppiumBy.ID, 'com.iherb:id/myaccount_dest').click()
        return MyAccountScreen()
