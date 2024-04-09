import {actions} from "./actions";
import {data} from "./data";
import {utils} from "./utils";

describe('Поиск товара в каталоге', () => {

    beforeEach(() => {
        cy.visit('/')
    })

    it('Пользователь может искать товар через поиск', () => {
        actions.getSearchField().type(data.searchText).should('have.value', data.searchText)
        actions.getSearchButton().click()
        actions.getBreadcrumb().contains(utils.getBreadcrumbText(data.searchText))
        cy.url().should('include', utils.getSearchUrl(data.searchText))
        cy.title().should('eq', utils.getSearchTitlePage(data.searchText))
    })

    it('Пользователь может искать товар через карточки', () => {
        actions.getAboutLink().click()
        actions.getBreadcrumb().contains(data.searchByCard.text)
        cy.url().should('include', data.searchByCard.url)
        cy.title().should('eq', data.searchByCard.text)
        actions.getFilter(data.filter.text).click()
        cy.url().should('include', utils.getFilterUrl(data.searchByCard.url, data.filter.id))
    })

    it('Пользователь может переходить по контенту страницы', () => {
        actions.getProductItem(data.productItem.text).click()
        actions.getProductTitle(data.productItem.text).should('have.text', data.productItem.text)
        cy.url().should('include', data.productItem.url)
        cy.title().should('eq', data.productItem.text)
    })

    it('Пользователь может искать по категориям', () => {
        actions.getMenuItem(data.category.text).click()
        actions.getBreadcrumb().contains(data.category.text)
        cy.url().should('include', data.category.url)
        cy.title().should('eq', data.category.text)
    })
})
