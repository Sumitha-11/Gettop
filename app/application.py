from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.footer_page import FooterPage
from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


class Application:

    def __init__(self,driver):
        self.driver = driver

        self.cart_page     = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.header        = Header(self.driver)
        self.footer_page   = FooterPage(self.driver)
        self.login_page    = LoginPage(self.driver)
        self.main_page     = MainPage(self.driver)
        self.product_page  = ProductPage(self.driver)