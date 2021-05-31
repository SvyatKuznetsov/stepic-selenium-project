from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.browser.current_url
        login_str = "login"
        assert False, "Opened not login page"
        # assert login_str in cur_url, "Opened not login page"

    def should_be_login_form(self):
        assert False, "Login form is not presented"
        # assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert False, "Register form is not presented"
        # assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"