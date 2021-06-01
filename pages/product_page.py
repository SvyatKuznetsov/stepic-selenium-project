from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def guest_can_see_product_name(self):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        assert product_name_in_store.text == product_name_in_basket.text, "Product name is no the same"

    def product_price_is_correct(self):
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET)
        product_price_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_STORE)
        assert product_price_in_store.text == product_price_in_basket.text, "Product price is wrong"

    def check_message_about_adding_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_disappearing_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message didn`t disappearing, but should"
