from pages.base_page import BasePage, NextPage
import time
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def fill_login_credentials(self, email, password):
        self.element_is_visible(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_sign_in_button(self):
        self.element_is_visible(LoginPageLocators.SIGN_IN_BUTTON).click()

    def click_sign_up_button(self):
        self.element_is_visible(LoginPageLocators.SIGN_IN_BUTTON).click()

    def fill_sign_up_data(self, name, email, password):
        self.element_is_visible(LoginPageLocators.NAME_INPUT).send_keys(name)
        self.element_is_visible(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def get_sign_up_confirmation_text(self):
        text = self.element_is_visible(LoginPageLocators.SIGN_UP_CONFIRMATION_TEXT).text
        return text
