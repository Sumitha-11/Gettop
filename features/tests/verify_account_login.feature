# Created by USER at 18-02-2022
Feature: Test Scenario for account login page

  Scenario: opens login page with all UI elements
    Given Open gettop login page
    Then  Verify email,password and remember me UI elements are present in the login page
    When  Verify LOG IN UI element is present
    Then  Verify Lost your password? ui element is present

  Scenario: User can click on Lost your password link and is taken to password reset form
    Given Open gettop login page
    When  Click on Lost your password link
    Then  Verify Reset password link is displayed

  Scenario: User can see Best Selling, Latest, Top Rated blocks
    Given Open gettop login page
    Then  Verify User can see Best Selling, Latest, Top Rated blocks