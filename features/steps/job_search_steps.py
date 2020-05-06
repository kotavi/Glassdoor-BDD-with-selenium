import time

from behave import step
from nose.tools import assert_true, assert_in, assert_not_in

from features.pages.job_search_page import JobSearchPage


@step('User searches jobs for "{job_title}" in location "{location}"')
def step_impl(context, job_title, location):
    page = JobSearchPage(context)
    page.job_title.send_keys(job_title)
    # page.suggestion_menu.click()

    page.job_location.clear()
    page.job_location.send_keys(location)

    popup = page.find_element(*page.locator_dictionary['add_your_resume']).is_displayed()
    if popup:
        # button = page.find_element(*page.locator_dictionary['finish_profile_button'])
        close_button = page.find_element(*page.locator_dictionary['close_button'])
        close_button.click()
    # time.sleep(1)
    # element = WebDriverWait(page.browser, page.timeout).until(
    #     EC.presence_of_element_located(page.locator_dictionary['search_button'])
    # )
    # element.click()
    page.search_button.click()


@step('A list of jobs is returned')
def step_impl(context):
    page = JobSearchPage(context).JobResults(context)
    assert_true(page.find_element(*page.locator_dictionary['results']).is_displayed())


@step('Job was not found')
def step_impl(context):
    page = JobSearchPage(context).JobResults(context)
    element = page.find_element(*page.locator_dictionary['job_not_found_message'])
    assert_in("does not match any jobs", element.text)


@step('The location name {name} is changed')
def step_impl(context, name):
    page = JobSearchPage(context)
    element = page.find_element(*page.locator_dictionary['job_location'])
    assert_not_in(name, element.text)


@step('User clicks on the first job in the list')
def step_impl(context):
    page = JobSearchPage(context).JobResults(context)
    page.first_job.click()


@step('The job description appears on the right')
def step_impl(context):
    page = JobSearchPage(context).JobResults(context)
    assert_true(page.find_element(*page.locator_dictionary['job_description']).is_displayed())


@step('The job title is correct')
def step_impl(context):
    page = JobSearchPage(context).JobResults(context)
    assert_true(page.first_job_name.text in page.chosen_job_employer.text)
