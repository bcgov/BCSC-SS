// Visit a web page
import "cypress-keycloak-commands";
describe('BC Keycloak Test', function()
{
    it('Visit the BC Dev Page and Login as Analyst', function()
    {
        cy.log("Visiting the BC Services Card [DEV] URL")
        cy.visit('https://selfservice-dev.pathfinder.gov.bc.ca/')
        cy.wait(10000)
        cy.log("Searching for the Login Button")
        cy.contains('Login').click()
        cy.wait(5000)
        cy.log("Fetching details from Json file and validating with Keycloak")
        cy.kcLogout();
        //Testing Login for analyst
        cy.log("Logging in as Analyst")
        cy.kcLogin("analyst");
        cy.wait(5000)
        cy.log("Successfully logged in and directed to Dashboard")
        cy.visit("https://selfservice-dev.pathfinder.gov.bc.ca/dashboard");
        cy.wait(5000)
        cy.log("Test Complete")
    })
})