@tags @tag
Feature: Job search

  As a user I want to be able to perform a job search by titles, and locations
  So that I would get a list of posted jobs and see their description

  Background:
    Given User navigates to signup page
      When User logs in with valid credentials
      Then Page should have an expected title "Glassdoor Job Search | Find the job that fits your life"

  @negative
  Scenario: Having entered a wrong job name the search returns 0 results
    When User searches jobs for "Aditojuohi" in location "Austin, TX (US)"
    Then Job was not found

  @negative
  Scenario: User cannot enter a wrong location name
    When User searches jobs for "Tester" in location "Razdolnoe"
    Then The location name "Razdolnoe" is changed