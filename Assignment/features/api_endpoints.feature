Feature: API Interaction Testing

  Scenario: Get a non-existing user
    Given I am on the home page
    When I select "GET SINGLE USER NOT FOUND"
    Then I should see the response status code "404"
    Then I should see the response contains "{}"

  Scenario: Get user list
    Given I am on the home page
    When I select "GET USER LIST"
    Then I should see the response status code "200"
    Then I should see the response contains "data"

  Scenario: Create a new user
    Given I am on the home page
    When I select "POST CREATE USER"
    Then I should see the response status code "201"
    Then I should see the response contains "Jane Doe"