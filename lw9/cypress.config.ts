import {defineConfig} from "cypress";

export default defineConfig({
    e2e: {
        baseUrl: 'http://shop.qatl.ru/',
        setupNodeEvents() {
            // implement node event listeners here
        },
        supportFile: false,
        specPattern: './lw/lw9/cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
    },
});
