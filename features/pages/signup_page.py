__author__ = 'pmacharl'
from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from configs.config import settings


class SignupPage(BasePage):

    locator_dictionary = {
        "signin_button": (By.CLASS_NAME, 'sign-in'),
        "signedin_button": (By.CLASS_NAME, 'signed-in'),
        "signout_button": (By.CSS_SELECTOR, '.sign-out.antiBtn'),
    }

    TITLE = 'Glassdoor Job Search | Find the job that fits your life'

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=settings['url'])

    class SignInWindow(BasePage):
        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser,
                base_url=settings['url'])

        locator_dictionary = {
            "signin_modal": (By.CLASS_NAME, 'minh-modal'),
            "signin_button": (By.XPATH, "//button[@type='submit' and text()='Sign In']"),
            "address": (By.NAME, 'username'),
            "password": (By.NAME, 'password')
        }

        def login(self, username=settings['user']['username'], password=settings['user']['password']):
            self.find_element(*self.locator_dictionary['email']).send_keys(username)
            self.find_element(*self.locator_dictionary['password']).send_keys(password)
            self.find_element(*self.locator_dictionary['signin_button']).click()
