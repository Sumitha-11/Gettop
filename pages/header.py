from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):

    HOVER_WATCH = (By.CSS_SELECTOR, 'a[href="https://gettop.us/product-category/accessories/watch/"]')
    NUMBER_OF_WATCH_ITEMS = (By.CSS_SELECTOR, '#menu-item-471 ul.sub-menu a')
    HOVER_MAC = (By.CSS_SELECTOR, 'a[href="https://gettop.us/product-category/macbook/"]')
    NUMBER_OF_MAC_ITEMS = (By.CSS_SELECTOR, "#menu-item-468 ul.sub-menu a")
    MAC_PRODUCT_TITLE = (By.CSS_SELECTOR, "h1.product-title")



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

    def hover_over_MAC(self):
        mac_flag = self.find_element(*self.HOVER_MAC)
        action = ActionChains(self.driver)
        action.move_to_element(mac_flag)
        action.perform()

    def verify_all_mac_items(self,expected_count):
        actual_count = len(self.find_elements(*self.NUMBER_OF_MAC_ITEMS))
        assert int(expected_count) == actual_count,f"Actual {actual_count} does not match expected {expected_count}"

    def hover_and_click_mac_product(self):
        mac_flag = self.find_element(*self.HOVER_MAC)
        action = ActionChains(self.driver)
        action.move_to_element(mac_flag).perform()
        sub_link = (self.driver.find_elements(*self.NUMBER_OF_MAC_ITEMS))
        lists = []
        for link in sub_link:
            lists.append(link.get_attribute('href'))
        for i in range(len(lists)):
            expected_text = ['MacBook Pro 13-inch', 'MacBook Pro 16-inch', 'MacBook Air']
            self.driver.get(lists[i])
            actual_text = self.driver.find_element(*self.MAC_PRODUCT_TITLE).text
            assert expected_text[i] == actual_text, f"Actual doesnot match Expected"





