import {actions} from "./actions";
import {data} from "./data";

describe('Авторизация', () => {
    it('Пользователь может авторизоваться', () => {
        cy.visit('/');

        actions.getDropdownToggle().click()
        actions.getLoginButton().click()
        cy.url().should('include', data.authorizationUrl)

        actions.getLoginField().type(data.user.login).should('have.value', data.user.login)
        actions.getPasswordField().type(data.user.password).should('have.value', data.user.password)
        actions.getSubmitButton().click()

        cy.contains(data.messageText)
    })
})
