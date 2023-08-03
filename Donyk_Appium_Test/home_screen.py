from appium.webdriver.common.appiumby import AppiumBy
from Donyk_Appium_Test.search_results_screen import SearchResultsScreen
from Donyk_Appium_Test.my_account_screen import MyAccountScreen


class HomeScreen:

    def __init__(self, driver):
        self.driver = driver

    def search(self, keyword):
        search_bar = self.driver.find_element(AppiumBy.XPATH, '//*[@text="Search iHerb"]')
        search_bar.click()
        search_field = self.driver.find_element(AppiumBy.XPATH, '//*[@text="Search iHerb"]')
        search_field.send_keys(keyword)
        self.driver.execute_script('mobile: performEditorAction', {"action": "search"})
        return SearchResultsScreen(self.driver)

    def open_my_account_screen(self):
        my_account_icon = self.driver.find_element(AppiumBy.XPATH, '(//*[@resource-id="com.iherb:id/navigation_bar_item_icon_view"])[4]')
        my_account_icon.click()
        return MyAccountScreen(self.driver)
