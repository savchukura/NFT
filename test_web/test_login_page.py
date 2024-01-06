from pages.login_page import LoginPage
from data.data import *
import time


class TestLoginPage:

    def test_valid_login(self, driver):
        login = LoginPage(driver, BASE_URL)
        login.open()
        login.fill_login_credentials(BASE_USER['email'], BASE_USER['password'])
        login.click_sign_in_button()
        time.sleep(5)
