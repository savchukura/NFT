from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a[class='text-sm text-primary-700 font-bold']")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "a[class='font-bold text-primary-700 cursor-pointer']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    GET_STARTED_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "a[class='text-sm font-normal text-error-500']")

    SIGN_UP_CONFIRMATION_TEXT = By.CSS_SELECTOR, "h1[class='text-4xl font-bold mb-3']"
