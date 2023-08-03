from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from Omelchenko_AppiumTest.AppiumPageObjectClasses.my_account_page import MyAccountPage
from Omelchenko_AppiumTest.AppiumPageObjectClasses.search_results_page import SearchResultsPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search(self, search_keyword) -> SearchResultsPage:
        search_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Search iHerb']")
        search_field.click()
        search_box = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Search iHerb']")
        search_box.send_keys(search_keyword)
        # This needed to perform search action, because .sendKeyEvent(84) doesn't work
        # self.driver.execute_script('mobile: performEditorAction', {"action": "search"})
        TouchAction(self.driver).tap(None, 991, 2098, 1).perform()
        return SearchResultsPage(self.driver)

    def open_my_account(self) -> MyAccountPage:
        my_account_icon = self.driver.find_element\
            (AppiumBy.XPATH, "(//*[@resource-id='com.iherb:id/navigation_bar_item_icon_view'])[4]")
        my_account_icon.click()
        return MyAccountPage(self.driver)
