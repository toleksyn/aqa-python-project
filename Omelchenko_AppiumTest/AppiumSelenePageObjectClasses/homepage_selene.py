from appium.webdriver.common.appiumby import AppiumBy
from selene import browser

from Omelchenko_AppiumTest.AppiumSelenePageObjectClasses.search_results_page_selene import SearchResultsPage


class HomePage:
    def search(self, search_keyword) -> SearchResultsPage:
        search_field = browser.element((AppiumBy.XPATH, "//*[@text='Search iHerb']"))
        search_field.click()
        search_box = browser.element((AppiumBy.XPATH, "//*[@text='Search iHerb']"))
        search_box.send_keys(search_keyword)
        # This needed to perform search action, because .sendKeyEvent(84) doesn't work
        browser.execute_script('mobile: performEditorAction', {"action": "search"})
        return SearchResultsPage()
