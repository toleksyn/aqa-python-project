from appium.webdriver.common.appiumby import AppiumBy

class IherbFilterAndSorterDrawer:
    def __init__(self, driver):
        self.driver = driver

    def set_brands_filter(self, brand_name):
        brands_dropdown = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Brands']")
        brands_dropdown.click()
        brands_checkbox = self.driver.find_element \
            (AppiumBy.XPATH, "//android.widget.Checkbox[starts-with(@text, '{}')]").format(brand_name)
        brands_checkbox.click()
        apply_button = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.iherb:id/bt_filter_apply']")
        apply_button.click()
        from iherb_search_results_screen import IherbSearchResultsScreen
        return IherbSearchResultsScreen(self.driver)