from behave import step
from nose.tools import assert_equal, assert_true
from features.pages.signup_page import SignupPage


@step('Page should have an expected title "{title}"')
def step_impl(context, title):
    page = SignupPage(context)
    assert_equal(page.title(), title)


@step('Page with title "{title}" will be opened')
def step_impl(context, title):
    page = SignupPage(context)
    assert_equal(title, page.title())