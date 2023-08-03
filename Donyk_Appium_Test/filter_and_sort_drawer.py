from appium.webdriver.common.appiumby import AppiumBy


class FilterAndSortDrawer:

    def __init__(self, driver):
        self.driver = driver

    def set_brands_filter(self, filter_name):
        brands_list = self.driver.find_element(AppiumBy.XPATH, '//*[@text="Brands"]')
        brands_list.click()
        filter_checkbox = self.driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[starts-with(@text, "{}")]'.format(filter_name))
        filter_checkbox.click()
        apply_button = self.driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.iherb:id/bt_filter_apply"]')
        apply_button.click()
        from Donyk_Appium_Test.search_results_screen import SearchResultsScreen
        return SearchResultsScreen(self.driver)
