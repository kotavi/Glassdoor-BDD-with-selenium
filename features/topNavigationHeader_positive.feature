@tags @tag
Feature: Top navigation header

  As a user I want to be able to use top navigation

  Background:
    Given User navigates to signup page
      And User logs in with valid credentials

  @smoke @positive
  Scenario Outline: User can open <Test name> top navigation link
      When User clicks on "<Link Name>" link
      Then Page with title "<Title>" will be opened

    Examples:
    | Test name         | Link Name          | Title                                             |
    | Jobs              |  jobs              | My Jobs \| Glassdoor                              |
    | Reviews           |  reviews           | Companies & Reviews \| Glassdoor                  |
    | Salaries          |  salaries          | Company Salaries \| Glassdoor                     |
    | Interview         |  interviews        | Interview Questions & Answers \| Glassdoor        |
    | Salary Calculator |  salary calculator | Salary Calculator - Know Your Worth \| Glassdoor  |