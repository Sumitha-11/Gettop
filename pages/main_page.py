from pages.base_page import Page

class MainPage(Page):
    def open_gettop(self):
        self.open_page()

    def open_login_page(self):
        self.open_page(f'my-account/')
