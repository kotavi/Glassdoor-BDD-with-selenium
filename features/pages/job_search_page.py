from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from configs.config import settings


class JobSearchPage(BasePage):
    locator_dictionary = {
        "job_title": (By.XPATH, "//input[@name='sc.keyword']"),
        "suggestion_menu": (By.XPATH, "//div[@class='autocomplete-suggestions ']//div[@data-val='Quality Assurance Engineer']"),
        "job_location": (By.XPATH, "//input[@id='sc.location']"),
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
            "first_job": (By.XPATH, "//div//ul[@class='jlGrid hover']//li[1]"),
            "first_job_name": (By.XPATH, "//li[1]//div[@class='jobInfoItem jobEmpolyerName']"),
            # TODO: fix, as it returns 31 objects
            "selected_job": (By.XPATH, "//div[@class='jobInfoItem jobEmpolyerName']"),
            "chosen_job": (By.XPATH, "//div[@id='JDCol']"),
            "chosen_job_employer": (By.XPATH, "//div[@class='employerName']"),
            "job_description": (By.XPATH, "//div[@id='JobDescriptionContainer']"),
            # TODO: fix, as it returns 31 objects
            "heart": (By.XPATH, "//i[@class='heart']"),
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser,
                base_url=settings['url'])
