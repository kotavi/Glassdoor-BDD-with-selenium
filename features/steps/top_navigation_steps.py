from behave import step

from features.pages.top_navigation_header_page import TopNavigationHeaderPage


@step('User clicks on "{menu_name}" link')
def step_impl(context, menu_name):
    page = TopNavigationHeaderPage(context)
    page.click_menu(menu_name)
