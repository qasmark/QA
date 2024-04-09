import {data} from "./data";

function getSearchUrl(text: string) {
    return data.searchUrl + '?s=' + text
}

function getSearchTitlePage(text: string) {
    return 'Поиск по: ' + text
}

function getBreadcrumbText(text: string) {
    return `Поиск по запросу "${text}"`
}

function getFilterUrl(url: string, text: string) {
    return url + '?filter=' + text
}

const utils = {
    getSearchUrl,
    getSearchTitlePage,
    getBreadcrumbText,
    getFilterUrl,
}

export {
    utils,
}
