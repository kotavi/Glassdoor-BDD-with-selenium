@tags @tag
Feature: Salary Calculator

  As a user I want to be able to get my personalized salary estimate based on today's job market

  @smoke @positive
  Scenario: User can get personalized salary estimate
    Given User navigates to signup page
      And User logs in with valid credentials
      And User clicks on "salary calculator" link
      Then Page with title "Salary Calculator - Know Your Worth | Glassdoor" will be opened
      And Sleep
