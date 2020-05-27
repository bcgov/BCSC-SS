// Import Cypress Keycloak commands
// Log in as Analyst and Load Test Accounts
import "cypress-keycloak-commands";
describe('BC Dev Login Test for Analyst', function()
{
    it('Visit the BC Dev Page and Login as Analyst', function(){
        cy.log("Visiting the BC Services Card [DEV] URL")
        cy.visit('https://selfservice-dev.pathfinder.gov.bc.ca/')
        cy.wait(5000)
        //Find the Login button
        cy.log("Searching for the Login button")
        cy.contains('Login').click()
        cy.wait(5000)
        //Make sure to logout of any previous Keycloak sessions
        cy.log("Logging out of previous Keycloak session")
        cy.kcLogout();
        cy.log("Fetching details from Json file and validating with Keycloak")
        cy.wait(5000)
        //Logging in as Analyst via Keycloak (Picks up values from users/analyst.json)
        cy.log("Log In as Analyst")
        cy.kcLogin("analyst");
        cy.wait(5000)
        cy.log("Log in successful and user is directed to Dashboard")
        cy.visit("https://selfservice-dev.pathfinder.gov.bc.ca/dashboard");
        cy.wait(5000)
        cy.log("Analyst can view Remaining test accounts right above the dashboard")
        cy.log("Displays the remaining test accounts")
        cy.contains('test accounts remaining')
        //Click on Load Test Accounts
        cy.log("Click on Manage Test Accounts")
        cy.get('[data-test-id="btn-create-test-account"]').click()
        cy.wait(5000)
        cy.log("Redirected to Add Test Account Page")
        cy.wait(10000)
        cy.visit('https://selfservice-dev.pathfinder.gov.bc.ca/add-test-account')
        cy.wait(5000)
        cy.log("Paste csv contents in text area")
        cy.wait(5000)
        cy.contains('Paste your CSV in this text box')
        cy.wait(5000)
      
        cy.get('#test-account-text').type('SS4BPS201,98901,ONE,SS4BPS Felecia,F,4732 Easy Street,Highlands BC V9B 3V9,V9B 3V9,1998-04-30{enter}')
        cy.wait(5000)
        cy.get('#test-account-text').type('SS4BPS202,98902,TWO,SS4BPS Benjamin ,M,308-2464 Crimson Vale,Penticton BC V2A 5N1,V2A 5N1,2000-11-18{enter}')
        cy.wait(5000)
        cy.get('#test-account-text').type('SS4BPS203,98903,THREE,SS4BPS Tyisha,F,3853 Lazy Road,Alexis Creek BC V0L 3I3,V0L 3I3,1999-03-19{enter}')
        cy.wait(5000)
        cy.log("Click : Import")
        cy.get('[data-test-id="btn-test-account"]').click()
        cy.wait(1000)
        cy.log("Should display number of test accounts loaded or skipped")
        cy.log("Test Complete")
    })
    })