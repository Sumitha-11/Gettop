# Created by USER at 16-02-2022
Feature: Test Scenarios for checkout page

  Scenario: User can fill out checkout form after adding a product to cart and verify required fields are not blank
    Given Open gettop page
    Then  Click on WATCH
    And   Click on watch series 5 product
    Then  Add the product to cart
    When  Click on cart icon
    And   Click on PROCEED TO CHECKOUT button
    When  User can enter firstname firstname in the checkout form
    And   user can enter lastname lastname in the checkout form
    And   User can enter company_name company name in the checkout form
    Then  User can select US country from country drop down
    And   User can enter valid street address
    Then  User can enter correct city
    And   User can select any state
    Then  User can enter correct zipcode
    And   User can enter valid phone number
    Then  User can enter valid email address
    And   User can enter additional information if needed
    Then  Verify user cannot leave any required fields blank

  Scenario Outline: User can select any country from country drop down
    Given Open gettop page
    Then  Click on WATCH
    And   Click on watch series 5 product
    Then  Add the product to cart
    When  Click on cart icon
    And   Click on PROCEED TO CHECKOUT button
    Then  User can select <any> country from country drop down
    Then  Verify <selected_country> country is displayed
    Examples:
    |  any            | selected_country       |
    | IN              | India                  |
    | US              | United States (US)     |
    | GB              | United Kingdom (UK)    |

  Scenario: User sees correct errror message if clicking 'Place Order' when a required field not populated
    Given Open gettop page
    Then  Click on WATCH
    And   Click on watch series 5 product
    Then  Add the product to cart
    When  Click on cart icon
    And   Click on PROCEED TO CHECKOUT button
    Then  Click on place order
    And   Verify correct error message is displayed

  Scenario: User can go back to Cart by clicking 'Shopping Cart'
    Given Open gettop page
    Then  Click on WATCH
    And   Click on watch series 5 product
    Then  Add the product to cart
    When  Click on cart icon
    And   Click on PROCEED TO CHECKOUT button
    When  Click on Shopping cart
    Then  Verify user can see cart page after clicking shopping cart


