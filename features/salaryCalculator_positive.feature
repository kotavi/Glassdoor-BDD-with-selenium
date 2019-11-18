@tags @tag
Feature: Salary Calculator

  As a user I want to be able to get my personalized salary estimate based on today's job market

  Background:
    Given User navigates to signup page
      When User logs in with valid credentials
      Then Page should have an expected title "Glassdoor Job Search | Find the job that fits your life"

  @positive
  Scenario: User can get personalized salary estimate
    When User clicks on "salary calculator" link
      Then Page with title "Salary Calculator - Know Your Worth | Glassdoor" will be opened
    # TODO: finish the scenario

