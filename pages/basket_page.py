from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "There are products in basket, but should not be"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), \
            "There are not empty basket text, but should be"
