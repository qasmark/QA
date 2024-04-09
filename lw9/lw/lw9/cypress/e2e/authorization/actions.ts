function getDropdownToggle() {
    return cy.get('.dropdown-toggle')
}

function getLoginButton() {
    return cy.get('.dropdown-menu').contains('Вход')
}

function getLoginField() {
    return cy.get('input#login')
}

function getPasswordField() {
    return cy.get('input#pasword')
}

function getSubmitButton() {
    return cy.get('button[type="submit"]')
}

const actions = {
    getDropdownToggle,
    getLoginButton,
    getLoginField,
    getPasswordField,
    getSubmitButton,
}

export {
    actions,
}
