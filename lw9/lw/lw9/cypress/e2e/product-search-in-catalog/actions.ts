function getSearchField() {
    return cy.get('input#typeahead')
}

function getSearchButton() {
    return cy.get('input[type="submit"]').first()
}

function getBreadcrumb() {
    return cy.get('.breadcrumb')
}

function getAboutLink() {
    return cy.get('.about-top a')
}

function getFilter(filter: string) {
    return cy.contains(filter)
}

function getProductItem(text: string) {
    return cy.contains(text)
}

function getProductTitle(title: string) {
    return cy.get('.simpleCart_shelfItem').contains(title)
}

function getMenuItem(text: string) {
    return cy.get('.menu').contains(text)
}

const actions = {
    getSearchField,
    getSearchButton,
    getBreadcrumb,
    getAboutLink,
    getFilter,
    getProductItem,
    getProductTitle,
    getMenuItem,
}

export {
    actions,
}
