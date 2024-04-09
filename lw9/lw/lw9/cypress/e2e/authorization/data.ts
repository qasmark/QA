function getUserData() {
    return {
        login: 'qwerty123qwerty123',
        password: 'qwerty123qwerty123',
    }
}

function getAuthorizationUrl() {
    return '/user/login'
}

function getMessageText() {
    return 'Вы успешно авторизованы'
}

const data = {
    user: getUserData(),
    authorizationUrl: getAuthorizationUrl(),
    messageText: getMessageText(),
}

export {
    data,
}
