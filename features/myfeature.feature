Feature: OrangeHRM Logo
    Scenario: Logo presence on OrangeHRM home page
        Given launch firefox browser
        When open orange hrm page
        Then verify that logo present on page
        And close browser