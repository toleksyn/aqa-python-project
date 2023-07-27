from appium.webdriver.common.appiumby import AppiumBy
from Omelchenko_AppiumTest.AppiumPageObjectClasses.search_results_page_appium import SearchResultsPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search(self, search_keyword) -> SearchResultsPage:
        search_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Search iHerb']")
        search_field.click()
        search_box = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Search iHerb']")
        search_box.send_keys(search_keyword)
        # This needed to perform search action, because .sendKeyEvent(84) doesn't work
        self.driver.execute_script('mobile: performEditorAction', {"action": "search"})
        return SearchResultsPage(self.driver)
