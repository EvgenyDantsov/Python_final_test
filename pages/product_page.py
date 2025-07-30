from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_basket_page(self):
        super().go_to_basket_page()
        return BasketPage(self.browser, self.browser.current_url)

    def should_be_product_page(self):
        self.should_be_add_button()
        self.add_to_basket()
        self.should_be_correct_product_name()
        self.should_be_correct_product_price()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET), \
            "Add to basket button is not presented"

    def add_to_basket(self):
        button_basket = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.BUTTON_BASKET)
        )
        button_basket.click()
        #self.solve_quiz_and_get_code()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but should have"

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert product_name == alert_name, "Wrong product name in alert"

    def should_be_correct_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        assert product_price == alert_price, "Wrong price in alert"
