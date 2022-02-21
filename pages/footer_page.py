from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page

class FooterPage(Page):
    COPYRIGHT_FOOTER = (By.CSS_SELECTOR,"div.copyright-footer")
    FOOTER_BUTTON = (By.CSS_SELECTOR,"#footer a[href='#top']")
    FOOTER_CATEGORIES = (By.CSS_SELECTOR,"div.footer-widgets span.widget-title")
    FOOTER_PRODUCT_LINKS = (By.CSS_SELECTOR,"div.footer-widgets div.woocommerce ul.product_list_widget a")
    GETTOP_LOGO = (By.ID,"logo")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.footer-widgets div.woocommerce ul.product_list_widget span.product-title")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.footer-widgets div.woocommerce ul.product_list_widget span.woocommerce-Price-amount")
    PRODUCT_RATING = (By.CSS_SELECTOR,".product_list_widget .star-rating")

    def verify_footer_category(self):
        expected_result = ['BEST SELLING', 'LATEST', 'TOP RATED']
        actual_result = []
        footer_title = self.driver.find_elements(*self.FOOTER_CATEGORIES)
        for title in footer_title:
            actual_result.append(title.text)
        assert actual_result == expected_result, f'actual{actual_result} does not match expected{expected_result}'

    def verify_product_name(self):
        expected_result = ['MacBook Pro 16-inch', 'AirPods Pro', 'AirPods with Wireless Charging Case',
                           'Watch Series 3', 'MacBook Air', 'MacBook Pro 16-inch', 'iPhone SE', 'iPhone 11',
                           'iPhone SE', 'MacBook Air', 'MacBook Pro 16-inch']
        product_name = self.driver.find_elements(*self.PRODUCT_TITLE)
        for name in range(len(product_name)):
            actual_result = product_name[name].text
            assert expected_result[name] == actual_result, f'actual {actual_result} doesnot match expected {expected_result}'

    def verify_product_price(self):
        expected_result = ['$2,399.00', '$249.00', '$199.00', '$199.00', '$999.00', '$2,399.00', '$399.00', '$379.00',
                           '$699.00', '$399.00', '$379.00', '$999.00', '$2,399.00']
        product_price = self.driver.find_elements(*self.PRODUCT_PRICE)
        for price in range(len(product_price)):
            actual_result = product_price[price].text
            assert expected_result[price] == actual_result, f'actual {actual_result} doesnot match expected {expected_result}'

    def verify_product_rating(self,expected_count):
        actual_count = len(self.find_elements(*self.PRODUCT_RATING))
        assert int(expected_count) == actual_count,f'Actual {actual_count} does not match Expected {expected_count}'

    def verify_copyright(self,expected_text):
        actual_text = self.find_element(*self.COPYRIGHT_FOOTER).text
        assert expected_text in actual_text,f'Expected {expected_text}, but got {actual_text}'

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_footer_button(self):
        flag = self.find_element(*self.FOOTER_BUTTON)
        action = ActionChains(self.driver)
        action.move_to_element(flag)
        action.click().perform()

    def gettop_logo_appears(self):
        assert self.find_element(*self.GETTOP_LOGO)

    def verify_footer_product_link(self):
        product_links = self.find_elements(*self.FOOTER_PRODUCT_LINKS)
        for link in range(len(product_links)):
            link = self.find_elements(*self.FOOTER_PRODUCT_LINKS)[link]
            link.click()
            assert (self.driver.current_url)
            self.driver.back()




