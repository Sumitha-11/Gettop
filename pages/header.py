from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):

    HOVER_WATCH = (By.CSS_SELECTOR, 'ul.header-nav a[href="https://gettop.us/product-category/accessories/watch/"]')
    NUMBER_OF_WATCH_ITEMS = (By.CSS_SELECTOR, '#menu-item-471 ul.sub-menu a')


    def hover_watch(self):
        flag = self.find_element(*self.HOVER_WATCH)
        action = ActionChains(self.driver)
        action.move_to_element(flag)
        action.perform()

    def verify_number_of_items(self,expected_count):
        actual_count = len(self.find_elements(*self.NUMBER_OF_WATCH_ITEMS))
        assert int(expected_count) == (actual_count), f'Actual {actual_count} does not match expected {expected_count}'

    def click_watch(self):
        self.click(*self.HOVER_WATCH)






