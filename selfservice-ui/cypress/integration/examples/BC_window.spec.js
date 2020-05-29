describe('Home Page Basic Test', function()
{
    it('Testing essential elements on home page', function()
    {
        const time_ms = 500
        const url = Cypress.config().baseUrl
        cy.log("Visiting the BC Services Card [DEV] URL")
        cy.visit(url)
        cy.wait(time_ms)
        cy.log("Looking for content : Beta")
        cy.contains('Beta')
        cy.wait(time_ms)
        cy.log("Looking for content : Login")
        cy.contains('Login')
        cy.wait(time_ms)
        cy.scrollTo('bottom')
        cy.log("Looking for content : Learn More")
        cy.contains('Learn more')
        cy.wait(time_ms)
        cy.log("Looking for content : Get Started")
        cy.contains('Get started')
        cy.wait(time_ms)
        cy.log("Test Completed")

    })
})