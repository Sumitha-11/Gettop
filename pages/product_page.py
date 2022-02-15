from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1.product-title')
    TOTAL_WATCH_PRODUCTS = (By.CSS_SELECTOR, 'p.name a')

    def click_and_verify_product(self):
        expected_text = ['Watch Series 3', 'Watch Series 5']
        total = self.find_elements(*self.TOTAL_WATCH_PRODUCTS)
        for i in range(len(total)):
            link = self.find_elements(By.CSS_SELECTOR, 'p.name a')[i]
            link.click()
            actual_text = self.find_element(*self.PRODUCT_TITLE).text
            assert expected_text[i] == actual_text, f"Actual text {actual_text} does not match Expected text {expected_text} "
            self.driver.back()
