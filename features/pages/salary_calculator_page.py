from selenium.webdriver.common.by import By

import time
from nose.tools import assert_equal, assert_true
from features.pages.base_page import BasePage
from configs.config import settings


class SalaryCalculatorPage(BasePage):
    locator_dictionary = {
        "logo": (By.XPATH, "//a[@aria-label='Glassdoor']"),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=settings['url'])
