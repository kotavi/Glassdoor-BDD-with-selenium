@tags @tag
Feature: Login to Glassdoor

  As a user with valid credentials
  I want to be able to login to Glassdoor WebUI
  So that I would have access to its resources


  @smoke @positive
  Scenario: User can login to Glassdoor and logout
    Given User navigates to signup page
      When User logs in with valid credentials
      Then Page should have an expected title "Glassdoor Job Search | Find the job that fits your life"
      And User verifies that it was a successful login by logging out