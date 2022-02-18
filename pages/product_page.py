from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1.product-title')
    TOTAL_WATCH_PRODUCTS = (By.CSS_SELECTOR, 'p.name a')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,'button.single_add_to_cart_button')
    WATCH_SERIES_PRODUCT = (By.CSS_SELECTOR, ".product-title a[href*= 'ss-crew-california-sub-river-island/']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR,'a[href="https://gettop.us/checkout/"]')
    CART_ICON =(By.CSS_SELECTOR,".header-cart-title")

    def click_and_verify_product(self):
        expected_text = ['Watch Series 3', 'Watch Series 5']
        total = self.find_elements(*self.TOTAL_WATCH_PRODUCTS)
        for i in range(len(total)):
            link = self.find_elements(*self.TOTAL_WATCH_PRODUCTS)[i]
            link.click()
            actual_text = self.find_element(*self.PRODUCT_TITLE).text
            assert expected_text[i] == actual_text, f"Actual text {actual_text} does not match Expected text {expected_text} "
            self.driver.back()

    def click_product(self):
        self.click(*self.WATCH_SERIES_PRODUCT)

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)









