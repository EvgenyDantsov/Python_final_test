from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = (By.CSS_SELECTOR, "[href*='login']")

class ProductPageLocators():
    BUTTON_BASKET= (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert-success strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")