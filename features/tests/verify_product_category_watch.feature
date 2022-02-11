# Created by USER at 10-02-2022
Feature: Test scenario for product WATCH

  Scenario: User can see all items under WATCH
    Given Open gettop page
    Then Hover over WATCH
    Then Verify 2 items are shown under watch category


  Scenario: User can open each of the products under WATCH category, and correct pages open
    Given Open gettop page
    Then Click on WATCH
    And Click on each products and verify correct product_page is opened
