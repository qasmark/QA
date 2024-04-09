function getSearchText() {
    return 'ROYAL'
}

function getSearchUrl() {
    return '/search'
}

function getCategoryUrl(section: string) {
    return '/category' + section
}

function getSearchByCardData() {
    return {
        text: 'Royal London',
        url: getCategoryUrl('/royal-london'),
    }
}

function getFilterData() {
    return {
        text: 'Механика с автоподзаводом',
        id: '1',
    }
}

function getProductItem() {
    return {
        text: 'Casio GA-1000-1AER',
        url: '/product/casio-ga-1000-1aer',
    }
}

function getCategoryData() {
    return {
        text: 'Men',
        url: getCategoryUrl('/men'),
    }
}

const data = {
    searchText: getSearchText(),
    searchUrl: getSearchUrl(),
    searchByCard: getSearchByCardData(),
    filter: getFilterData(),
    productItem: getProductItem(),
    category: getCategoryData(),
}

export {
    data,
}
