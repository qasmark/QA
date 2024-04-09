function getProductItem(text: string) {
    return cy.contains('.product-main', text)
}

function getAddToCartIconButton() {
    return cy.get('.add-to-cart-link')
}

function getModalContent() {
    return cy.get('.modal-content')
}

function getTable() {
    return cy.get('.table')
}

function getItemTitle() {
    return cy.get('tr')
        .eq(1)
        .children()
        .eq(1)
}

function getItemCount() {
    return cy.get('tr')
        .eq(1)
        .children()
        .eq(2)
}

function getItemPrice() {
    return cy.get('tr')
        .eq(1)
        .children()
        .eq(3)
}

function getItemResultCount() {
    return cy.get('tr')
        .eq(2)
        .children()
        .eq(1)
}

function getItemResultPrice() {
    return cy.get('tr')
        .eq(3)
        .children()
        .eq(1)
}

function getModalButton(text: string) {
    return cy.get('.modal-footer').children().contains(text)
}

function getCartContent() {
    return cy.get('.table-responsive')
}

function getAddToCartButton() {
    return cy.get('#productAdd')
}

function getQuantityField() {
    return cy.get('input[name="quantity"]')
}

const actions = {
    getProductItem,
    getAddToCartIconButton,
    getModalContent,
    getTable,
    getItemTitle,
    getItemCount,
    getItemPrice,
    getItemResultCount,
    getItemResultPrice,
    getModalButton,
    getCartContent,
    getAddToCartButton,
    getQuantityField,
}

export {
    actions,
}
