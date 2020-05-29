// Visit a web page
import "cypress-keycloak-commands";
describe('BC Keycloak Test', function()
{   
    const time_ms = 500
    const url = Cypress.config().baseUrl
    it('Visit the BC Dev Page and Login as Analyst', function()
    {
        cy.log("Visiting the BC Services Card [DEV] URL")
        cy.visit(url)
        cy.url()
        cy.wait(time_ms)
        cy.log("Searching for the Login Button")
        cy.contains('Login').click()
        cy.wait(time_ms)
        cy.log("Fetching details from Json file and validating with Keycloak")
        cy.kcLogout();
        //Testing Login for analyst - Fetches details from json file in fixtures\users
        cy.log("Logging in as Analyst")
        //Fetches file "user_login"
        cy.kcLogin("user_login");
        cy.wait(time_ms)
        cy.log("Successfully logged in and directed to Dashboard")
        cy.visit(url+"/dashboard");
        cy.wait(time_ms)
        cy.log("Test Complete")
    })
})