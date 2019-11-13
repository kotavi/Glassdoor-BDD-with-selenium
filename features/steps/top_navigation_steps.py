from behave import step
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
import time
from configs.config import settings
from features.pages.signup_page import SignupPage

from features.pages.top_navigation_header_page import TopNavigationHeaderPage


@step('User clicks on "{menu_name}" link')
def step_impl(context, menu_name):
    page = TopNavigationHeaderPage(context)
    page.click_menu(menu_name)

# @step('Page with title "{title}" will be opened')
# def step_impl(context, title):
#     page = TopNavigationHeaderPage(context)
#     assert_equal(title, page.title())

