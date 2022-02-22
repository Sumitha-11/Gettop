from selenium.webdriver.common.by import By
from pages.base_page import Page

class LoginPage(Page):

    UI_ELEMENTS = (By.CSS_SELECTOR,".woocommerce-form label")
    LOGIN_BUTTON = (By.CSS_SELECTOR,"button[name='login']")
    LOST_YOUR_PASSWORD = (By.CSS_SELECTOR,'a[href="https://gettop.us/my-account/lost-password/"]')
    FOOTER_TITLE = (By.CSS_SELECTOR,".widget-title")

    def verify_UI_elements(self):
        expected_elements = ['Username or email address *', 'Password *', 'Remember me']
        ui_elements = self.find_elements(*self.UI_ELEMENTS)
        for element in range(len(ui_elements)):
            actual_elements = ui_elements[element].text
            assert expected_elements[element] == actual_elements,f'expected elements {expected_elements} does not match actual elements{actual_elements}'

    def verify_login_button(self,expected_text):
        self.verify_text(expected_text,*self.LOGIN_BUTTON)

    def lost_your_password(self,expected_text):
        self.verify_text(expected_text,*self.LOST_YOUR_PASSWORD)

    def click_lost_your_password(self):
        self.click(*self.LOST_YOUR_PASSWORD)

    def verify_reset_password_link(self):
        expected_link = "https://gettop.us/my-account/lost-password/"
        assert self.driver.current_url == expected_link ,f"actual_link does not match expected link"

    def verify_footer_title(self):
        expected_result = ['BEST SELLING', 'LATEST', 'TOP RATED']
        actual_result = []
        footer_title = self.driver.find_elements(*self.FOOTER_TITLE)
        for title in footer_title:
            actual_result.append(title.text)
        assert actual_result == expected_result, f'actual{actual_result} does not match expected{expected_result}'
