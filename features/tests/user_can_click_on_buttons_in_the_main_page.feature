# Created by Maddy at 3/14/2024
Feature: reelly.io main page tests


  Scenario: verifies user can click on “Connect the company”
    Given Open the log in page
    When Input sbronson38@gmail.com in email field
    Then Input IceCream18! in password field
    Then Click on continue button
    Then Click on “Connect the company”
    When Switch to the newly opened window
    Then Verify “Connect the company” page is opened




