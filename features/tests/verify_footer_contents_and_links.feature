# Created by USER at 14-02-2022
Feature: Test scenario for footer links and contents

  Scenario: User has to verify footer shows Best Selling, Latest, Top Rated categories
    Given Open gettop page
    Then  Verify footer shows BEST SELLING, LATEST, TOP RATED categories

  Scenario: User has to verify all products in the footer have name
    Given Open gettop page
    Then  Verify all products in the footer have name

  Scenario: User has to verify all products in the footer have price
    Given Open gettop page
    Then  Verify all products in the footer have price

  Scenario: User has to verify how many products in the footer have star rating
    Given Open gettop page
    Then  Verify 2 product has rating in the footer

  Scenario: User has to verify "Copyright 2022" shown in footer
    Given Open gettop page
    Then  Verify Copyright 2022 shown in footer

  Scenario: User has to verify footer has button to go back to top
    Given Open gettop page
    Then  Scroll to bottom of the page
    When  Click on footer button
    Then  Verify GetTop logo at the top of the page

  Scenario: User has to verify footer has working links to all product categories
    Given Open gettop page
    When  Click on footer product link and verify correct footer product link opens
