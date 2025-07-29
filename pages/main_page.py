from .base_page import BasePage
from .basket_page import BasketPage


class MainPage(BasePage):
    def go_to_basket_page(self):
        super().go_to_basket_page()
        return BasketPage(self.browser, self.browser.current_url)
