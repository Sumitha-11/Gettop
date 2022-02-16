# Created by USER at 15-02-2022
Feature:Test Sceanrios for MAC product

  Scenario:User can see all items under MAC
    Given Open gettop page
    When  Hover over MAC
    Then  Verify 3 items are shown under MAC category

  Scenario: User can open each of the products under MAC category, and correct pages open
    Given Open gettop page
    When  Hover over MAC and click on each products and verify correct product_page opens