function getProductUrl() {
    return '/product/casio-ga-1000-1aer'
}

function getUserData() {
    return {
        login: {
            busy: 'qwerty123qwerty123',
            free: 'Vladislav100',
        },
        password: 'qwerty123qwerty123',
        name: 'Влад',
        email: 'ignatyev@mail.ru',
        address: 'Yoshkar-Ola, 100',
        note: 'Оставить у двери',
    }
}

function getPlaceOrderButtonText() {
    return 'Оформить заказ'
}

function getErrorLoginMessageText() {
    return 'Этот логин уже занят'
}


const data = {
    productUrl: getProductUrl(),
    user: getUserData(),
    placeOrderButtonText: getPlaceOrderButtonText(),
    errorLoginMessageText: getErrorLoginMessageText()
}

export {
    data,
}
