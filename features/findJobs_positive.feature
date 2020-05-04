@tags @tag
Feature: Job search

  As a user I want to be able to perform a job search by titles, and locations
  So that I would get a list of posted jobs and see their description

  Background:
    Given User navigates to signup page
      When User logs in with valid credentials
      Then Page should have an expected title "Glassdoor Job Search | Find the job that fits your life"

#  @positive
#  Scenario: User performs a search by title and location
#    When User searches jobs for "tester qa engineer" in location "Austin, TX (US)"
#    Then A list of jobs is returned
#    When User clicks on the first job in the list
#     Then The job description appears on the right
#      And The job title is correct

  @negative
  Scenario: Having entered a wrong job name the search returns 0 results
    When User searches jobs for "Aditojuohi" in location "Austin, TX (US)"
    Then Job was not found
