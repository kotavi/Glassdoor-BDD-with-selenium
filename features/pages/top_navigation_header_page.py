from selenium.webdriver.common.by import By

import time
from nose.tools import assert_equal, assert_true
from features.pages.base_page import BasePage
from configs.config import settings


class TopNavigationHeaderPage(BasePage):
    locator_dictionary = {
        "logo": (By.XPATH, "//a[@aria-label='Glassdoor']"),
        "jobs": (By.XPATH, "//li[@class='jobs']//a[text()='Jobs']"),
        "reviews": (By.XPATH, "//li[@class='reviews']//a[text()='Company Reviews']"),
        "interviews": (By.XPATH, "//li[@class='interviews']//a[text()='Interviews']"),
        "salaries": (By.XPATH, "//li[@class='salaries']//a[text()='Salaries']"),
        "salary_calculator": (By.XPATH, "//li[@class='kyw']//a[text()='Salary Calculator']"),
        "account_settings": (By.XPATH, "//a//span[text()='Account Settings']"),
        "saved_jobs": (By.XPATH, "//a//span[@class='shape-heart']"),
        "write_review": (By.XPATH, "//a//span[text()='Write Review']"),
        "for_employers": (By.XPATH, "//a[text()='For Employers']"),
        "post_jobs_free": (By.XPATH, "//a[text()=' Post Jobs Free']"),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=settings['url'])

    def click_menu(self, menu_name):
        switcher = {
            "logo": self.find_element(*self.locator_dictionary['logo']),
            "jobs": self.find_element(*self.locator_dictionary['jobs']),
            "reviews": self.find_element(*self.locator_dictionary['reviews']),
            "salaries": self.find_element(*self.locator_dictionary['salaries']),
            "interviews": self.find_element(*self.locator_dictionary['interviews']),
            "salary calculator": self.find_element(*self.locator_dictionary['salary_calculator']),
        }
        return switcher[menu_name].click()
