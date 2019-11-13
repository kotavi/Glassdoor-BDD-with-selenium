from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from configs.config import settings


class SalaryCalculatorPage(BasePage):
    locator_dictionary = {
        "job_title": (By.XPATH, "//input[@name='sc.keyword']"),
        "job_location": (By.XPATH, "//input[@name='sc.location']"),
        "choice_list": (By.XPATH, "//ul[@class='context-choice-list']"),
        "search_button": (By.ID, "HeroSearchButton"),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=settings['url'])


    class JobResults(BasePage):

        locator_dictionary = {
            "results": (By.XPATH, "//article[@id='MainCol']"),
            "jobs_column": (By.XPATH, "//ul[@class='jlGrid hover']"),
            "selected_job": (By.XPATH, "//div[@class='jobInfoItem jobEmpolyerName']"), # TODO: fix, as it returns 31 objects
            "chosen_job": (By.XPATH, "//div[@id='JDCol']"),
            "chosen_job_employer": (By.XPATH, "//div[@class='employerName']"),
            "heart": (By.XPATH, "//i[@class='heart']"), # TODO: fix, as it returns 31 objects


        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser,
                base_url=settings['url'])
