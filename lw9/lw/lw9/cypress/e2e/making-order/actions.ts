function getAddToCartButton() {
    return cy.get('#productAdd')
}

function getModalButton(text: string) {
    return cy.get('.modal-footer').children().contains(text)
}

function getLoginField() {
    return cy.get('input#login')
}

function getPasswordField() {
    return cy.get('input#pasword')
}

function getNameField() {
    return cy.get('input#name')
}

function getEmailField() {
    return cy.get('input#email')
}

function getAddressField() {
    return cy.get('input#address')
}

function getNoteField() {
    return cy.get('textarea[name="note"]')
}

function getSubmitButton() {
    return cy.get('button[type="submit"]')
}

const actions = {
    getAddToCartButton,
    getModalButton,
    getLoginField,
    getPasswordField,
    getNameField,
    getEmailField,
    getAddressField,
    getNoteField,
    getSubmitButton,
}

export {
    actions,
}
