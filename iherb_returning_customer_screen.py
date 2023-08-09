from appium.webdriver.common.appiumby import AppiumBy

from iherb_notifications_popup import IherbNotificationsPopup

class IherbReturningCustomerScreen:
    def __init__(self, driver):
        self.driver = driver

    def sign_in_with_credentials(self, username, password):
        username_input = self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.EditText")
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.EditText").click()
        username_input.send_keys(username)
        password_input = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='Password']")
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='Password']").click()
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
        sign_in_button.click()
        from iherb_home_screen import IherbHomeScreen
        return IherbHomeScreen(self.driver)

    def log_in_with_iherb_account(self, username, password) -> IherbNotificationsPopup:
        self.sign_in_with_credentials(username, password)
        return IherbNotificationsPopup(self.driver)

    def get_error_message_text(self):
        error_message = self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.widget.ListView/android.view.View")
        return error_message.text