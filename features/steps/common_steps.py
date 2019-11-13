from behave import step
import time
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
from configs.config import settings
from features.pages.base_page import BasePage
from features.pages.signup_page import SignupPage
from selenium.common.exceptions import NoSuchElementException


@step('Page should have an expected title "{title}"')
def step_impl(context, title):
    page = SignupPage(context)
    assert_equal(page.title(), title)

@step('Page with title "{title}" will be opened')
def step_impl(context, title):
    page = SignupPage(context)
    assert_equal(title, page.title())