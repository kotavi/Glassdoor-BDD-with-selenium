from behave import step
from nose.tools import assert_equal, assert_true
from configs.config import settings
from features.pages.signup_page import SignupPage


@step('User navigates to signup page')
def step_impl(context):
    page = SignupPage(context)
    page.visit(settings['url'])
    assert_equal(page.title(), SignupPage(context).TITLE)


@step('User logs in with valid credentials')
def step_impl(context):
    signup_page = SignupPage(context)
    signup_page.signin_button.click()
    page = SignupPage(context).SignInWindow(context)
    assert_true(page.find_element(*page.locator_dictionary['signin_modal']).is_displayed())
    page.address.send_keys(settings['user']['username'])
    page.password.send_keys(settings['user']['password'])
    page.signin_button.click()


@step('User verifies that it was a successful login by logging out')
def step_impl(context):
    signup_page = SignupPage(context)
    signup_page.signedin_button.click()
    signup_page.signout_button.click()


# @step('Page should have an expected title "{title}"')
# def step_impl(context, title):
#     page = SignupPage(context)
#     assert_equal(page.title(), title)

# @step('Page should have a link "{link_text}"')
# def step_impl(context, link_text):
#     assert_equal(context.login_page.get_page_link_by_text(link_text), link_text)
#
# @step('User receives error message "{error_message}"')
# def step_impl(context, error_message):
#     assert_equal(context.login_page.get_alert_text(), error_message)

# @step('Page should not have a link "{link_text}"')
# def step_impl(context, link_text):
#     try:
#         context.login_page.get_page_link_by_text(link_text)
#         not_found = False
#     except NoSuchElementException:
#         not_found = True
#     assert_true(not_found, "It is expected that link '%s' doesn't exist" % link_text)
