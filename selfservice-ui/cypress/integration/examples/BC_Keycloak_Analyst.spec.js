// Visit a web page
import "cypress-keycloak-commands";
describe('BC Keycloak Test', function()
{   
    const time_ms = 500
    it('Visit the BC Dev Page and Login as Analyst', function()
    {
        cy.log("Visiting the BC Services Card [DEV] URL")
        cy.visit('https://selfservice-dev.pathfinder.gov.bc.ca/')
        cy.wait(time_ms)
        cy.log("Searching for the Login Button")
        cy.contains('Login').click()
        cy.wait(time_ms)
        cy.log("Fetching details from Json file and validating with Keycloak")
        cy.kcLogout();
        //Testing Login for analyst
        cy.log("Logging in as Analyst")
        cy.kcLogin("analyst");
        cy.wait(time_ms)
        cy.log("Successfully logged in and directed to Dashboard")
        cy.visit("https://selfservice-dev.pathfinder.gov.bc.ca/dashboard");
        cy.wait(time_ms)
        cy.log("Test Complete")
    })
})