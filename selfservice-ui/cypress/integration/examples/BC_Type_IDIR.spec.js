// Visit a web page
describe('BC Keycloak Login with IDIR', function()
{
    const time_ms = 500
    const url = Cypress.config().baseUrl
    
    it('Visit the BC Dev Page and Login', function(){
        cy.log("Visiting the BC Services Card [DEV] URL")
        cy.visit(url)
        cy.wait(time_ms)
        cy.log("Searching for the Login Button")
        cy.contains('Login').click()
        cy.log("It should open up Login page")
        cy.wait(time_ms)
        cy.url().should('include','openid-connect')
        cy.log("Should contain a button called IDIR")
        cy.wait(time_ms)
        cy.contains('IDIR').click()
        cy.log("Clicking on the IDIR button should take user to logontest page")
        cy.wait(time_ms)
        cy.url().should('include','logontest7.gov.bc.ca')
        cy.wait(time_ms)
        cy.log("Logging in with IDIR")
        //Enter your username and password
        cy.get('#user').type('<your-username>').should('have.value', '<your-username>')
        cy.wait(time_ms)
        cy.get('#password').type('<your-password>',{ log: false })
        cy.wait(time_ms)
        cy.log("Click on Continue")
        cy.contains('Continue').click()
        cy.wait(time_ms)
        cy.log("If User is valid, user will be taken to Dashboard view")
        cy.url().should('include',url+'/dashboard')
        cy.wait(time_ms)
        cy.log("Test Complete")
        
    })
})