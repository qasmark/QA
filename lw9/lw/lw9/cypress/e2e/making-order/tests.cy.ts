import {actions} from "./actions";
import {data} from "./data";

describe('Оформление заказа', () => {
    it('Пользователь может оформить заказ', () => {
        cy.visit(data.productUrl)

        actions.getAddToCartButton().click()
        actions.getModalButton(data.placeOrderButtonText).click()

        actions.getLoginField().type(data.user.login.busy).should('have.value', data.user.login.busy)
        actions.getPasswordField().type(data.user.password).should('have.value', data.user.password)
        actions.getNameField().type(data.user.name).should('have.value', data.user.name)
        actions.getEmailField().type(data.user.email).should('have.value', data.user.email)
        actions.getAddressField().type(data.user.address).should('have.value', data.user.address)
        actions.getNoteField().type(data.user.note).should('have.value', data.user.note)
        actions.getSubmitButton().click()
        cy.contains(data.errorLoginMessageText)

        actions.getLoginField()
            .clear()
            .type(data.user.login.free).should('have.value', data.user.login.free)
        actions.getNoteField().type(data.user.note).should('have.value', data.user.note)
        actions.getSubmitButton().click()
    })
})
