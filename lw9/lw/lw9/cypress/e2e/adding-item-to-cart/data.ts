function getProductOneItem() {
    return {
        count: 1,
        price: 400,
    }
}

function getProductManyItem() {
    return {
        count: 5,
        price: 2000,
    }
}

function getProductItem() {
    return {
        text: 'Casio GA-1000-1AER',
        url: '/product/casio-ga-1000-1aer',
        oneItem: getProductOneItem(),
        fiveItem: getProductManyItem(),
    }
}

function getPlaceOrderButtonText() {
    return 'Оформить заказ'
}

const data = {
    productItem: getProductItem(),
    placeOrderButtonText: getPlaceOrderButtonText(),
    cartUrl: '/cart/view',
}

export {
    data,
}
