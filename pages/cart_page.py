from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    PLACE_ORDER = (By.ID,'place_order')
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR,'.checkout-button')

    def click_checkout(self):
        self.click(*self.PROCEED_TO_CHECKOUT)

    def cart_page_displayed(self):
        expected_page = "https://gettop.us/cart/"
        actual_page = self.driver.current_url
        assert expected_page == actual_page,f'actual {actual_page} doe not macth expected{expected_page}'