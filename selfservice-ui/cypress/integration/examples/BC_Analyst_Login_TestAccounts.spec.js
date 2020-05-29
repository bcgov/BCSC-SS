// Import Cypress Keycloak commands
// Log in as Analyst and Load Test Accounts
import "cypress-keycloak-commands";
describe('BC Dev Login Test for Analyst', function()
{
    //Declaring a variable to change wait time in between the test for recording videos. Time is in milliseconds
    const time_ms = 500
    it('Visit the BC Dev Page and Login as Analyst', function(){
        cy.log("Visiting the BC Services Card [DEV] URL")
        cy.visit('https://selfservice-dev.pathfinder.gov.bc.ca/')
        cy.wait(time_ms)
        //Find the Login button
        cy.log("Searching for the Login button")
        cy.contains('Login').click()
        cy.wait(time_ms)
        //Make sure to logout of any previous Keycloak sessions
        cy.log("Logging out of previous Keycloak session")
        cy.kcLogout();
        cy.log("Fetching details from Json file and validating with Keycloak")
        cy.wait(time_ms)
        //Logging in as Analyst via Keycloak (Picks up values from users/analyst.json)
        cy.log("Log In as Analyst")
        cy.kcLogin("analyst");
        cy.wait(time_ms)
        cy.log("Log in successful and user is directed to Dashboard")
        cy.visit("https://selfservice-dev.pathfinder.gov.bc.ca/dashboard");
        cy.wait(time_ms)
        cy.log("Analyst can view Remaining test accounts right above the dashboard")
        cy.log("Displays the remaining test accounts")
        cy.contains('test accounts remaining')
        //Click on Load Test Accounts
        cy.log("Click on Manage Test Accounts")
        cy.get('[data-test-id="btn-create-test-account"]').click()
        cy.wait(time_ms)
        cy.log("Redirected to Add Test Account Page")
        cy.wait(time_ms)
        cy.visit('https://selfservice-dev.pathfinder.gov.bc.ca/add-test-account')
        cy.wait(time_ms)
        cy.log("Paste csv contents in text area")
        cy.wait(time_ms)
        cy.contains('Paste your CSV in this text box')
        cy.wait(time_ms)
        //Enter a set of Test Accounts to test
        cy.get('#test-account-text').type('<Test Account1 and details comma separated>{enter}')
        cy.wait(time_ms)
        cy.get('#test-account-text').type('<Test Account2 and details comma separated>{enter}')
        cy.wait(time_ms)
        cy.get('#test-account-text').type('<Test Account3 and details comma separated>{enter}')
        cy.wait(time_ms)
        cy.log("Click : Import")
        cy.get('[data-test-id="btn-test-account"]').click()
        cy.wait(time_ms)
        cy.log("Should display number of test accounts loaded or skipped")
        cy.log("Test Complete")
    })
    })