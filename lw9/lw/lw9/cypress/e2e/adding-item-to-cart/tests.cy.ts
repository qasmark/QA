import {actions} from "./actions";
import {data} from "./data";
import {utils} from "./utils";

describe('Добавление товара в корзину', () => {

    function addItemToCart(countItem) {
        actions.getModalContent().within(() => {
            actions.getTable().within(() => {
                actions.getItemTitle().should('have.text', data.productItem.text)
                actions.getItemCount().should('have.text', countItem.count)
                actions.getItemPrice().should('have.text', data.productItem.oneItem.price)
                actions.getItemResultCount().should('have.text', countItem.count)
                actions.getItemResultPrice().should('have.text', utils.getStringInDollars(countItem.price))
            })
            actions.getModalButton(data.placeOrderButtonText).click()
        })

        cy.url().should('include', data.cartUrl)

        actions.getCartContent().within(() => {
            actions.getTable().within(() => {
                actions.getItemTitle().should('have.text', data.productItem.text)
                actions.getItemCount().should('have.text', countItem.count)
                actions.getItemPrice().should('have.text', data.productItem.oneItem.price)
                actions.getItemResultCount().should('have.text', countItem.count)
                actions.getItemResultPrice().should('have.text', utils.getStringInDollars(countItem.price) + ' ')
            })
        })
    }

    it('Пользователь может добавить товар на главной странице', () => {
        cy.visit('/')

        actions.getProductItem(data.productItem.text)
            .within(() => {
                actions.getAddToCartIconButton().click()
            })

        addItemToCart(data.productItem.oneItem)
    })

    it('Пользователь может добавить товар на детальной странице товара', () => {
        cy.visit(data.productItem.url)

        actions.getAddToCartButton().click()

        addItemToCart(data.productItem.oneItem)
    })

    it('Пользователь может добавить 5 товаров на детальной странице товара', () => {
        cy.visit(data.productItem.url)

        actions.getQuantityField()
            .clear()
            .type(`${data.productItem.fiveItem.count}`).should('have.value', `${data.productItem.fiveItem.count}`)
        actions.getAddToCartButton().click()

        addItemToCart(data.productItem.fiveItem)
    })
})
