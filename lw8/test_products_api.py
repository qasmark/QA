from os import path
from products_api import ProductsApi
import json
import jsonschema # type: ignore
import unittest
# [TODO]
# добавить проверкy значений Category, old_price, hit (только проверка на null)

class TestProductsApi(unittest.TestCase):
    _CONFIG_DIR = path.join(path.dirname(path.realpath(__file__)), 'cfg')

    _PRODUCTS_FILE = 'products.json'
    _PRODUCTS_SCHEMA_FILE = 'products.schema.json'

    def setUp(self):
        self._api = ProductsApi()
        self._created_product_ids = []
        self._products = self._load_config_json(self._PRODUCTS_FILE)
        self._products_schema = self._load_config_json(
                self._PRODUCTS_SCHEMA_FILE)

    def tearDown(self):
        for product_id in self._created_product_ids:
            self._api.delete(product_id)

    def test_CreatingValidProduct_AddsItToTheList(self):
        response = self._create_product(self._products['valid'])

        products = self._api.list()
        list_product = self._find_product(products, response['id'])

        self.assertTrue(
                self._products['valid'].items() <= list_product.items(),
                'product in list should match the request')

    def test_CreatingWithTheSameAlias_AddsPostfix(self):
        response1 = self._create_product(self._products['valid_for_alias'])
        response2 = self._create_product(self._products['valid_for_alias'])

        products = self._api.list()
        list_product1 = self._find_product(products, response1['id'])
        list_product2 = self._find_product(products, response2['id'])

        self.assertEqual(
                list_product1['alias'],
                self._products['valid_for_alias']['alias'],
                'first alias should match the original title')
        self.assertEqual(
                list_product2['alias'],
                self._products['valid_for_alias']['alias'] + '-0',
                'second alias should have -0 postfix')

    def test_CreatingWithInvalidPrice_ReturnsError(self):
        response = self._create_product(self._products['invalid_price'])

        self.assertEqual(response['status'], 0, 'response status should be 0')

    def test_CreatingWithInvalidCategory_ReturnsError(self):
        response = self._create_product(self._products['invalid_category'])

        self.assertEqual(response['status'], 0, 'response status should be 0')

    def test_CreatingWithInvalidStatus_ReturnsError(self):
        response = self._create_product(self._products['invalid_status'])

        self.assertEqual(response['status'], 1, 'response status should be 1')

    def test_CreatingWithInvalidHit_ReturnsError(self):
        response = self._create_product(self._products['invalid_hit'])

        self.assertEqual(response['status'], 1, 'response status should be 1')

    def test_CreatingWithMissingProps_ReturnsError(self):
        response = self._create_product(self._products['missing_props'])

        self.assertEqual(response['status'], 0, 'response status should be 0')

    def test_CreatingWithEmptyProduct_ReturnsError(self):
        response = self._create_product(self._products['empty'])

        self.assertEqual(response['status'], 0, 'response status should be 0')

    def test_CreatingWithNullProduct_ReturnsError(self):
        response = self._create_product(self._products['null'])

        self.assertEqual(response['status'], 0, 'response status should be 0')

    def test_EditingProduct_ChangesItInTheListAndUpdatesAlias(self):
        create_response = self._create_product(self._products['valid'])
        product = self._products['valid_updated']
        product['id'] = str(create_response['id'])
        response = self._api.edit(product)

        products = self._api.list()
        list_product = self._find_product(products, create_response['id'])

        self.assertEqual(response['status'], 1, 'response status should be 1')
        self.assertTrue(
                product.items() <= list_product.items(),
                'product in list should be updated')

    def test_EditingWithDuplicatingAlias_AddsIdPostfix(self):
        self._create_product(self._products['valid_updated'])
        create_response = self._create_product(self._products['valid'])

        product = self._products['valid_updated']
        product['id'] = str(create_response['id'])
        response = self._api.edit(product)

        products = self._api.list()
        list_product = self._find_product(products, create_response['id'])

        self.assertEqual(response['status'], 1, 'response status should be 1')
        self.assertEqual(
                list_product['alias'],
                self._products['valid_updated']['alias'] + '-' + product['id'],
                'product should have alias with ID postfix')

    def test_EditingOnlyTitle_ReturnsErrorAndChangesNothing(self):
        create_response = self._create_product(self._products['valid'])

        product = self._products['update_title']
        product['id'] = create_response['id']
        response = self._api.edit(product)

        products = self._api.list()
        list_product = self._find_product(products, create_response['id'])

        self.assertEqual(response['status'], 0, 'response status should be 0')
        self.assertTrue(
                self._products['valid'].items() <= list_product.items(),
                'original product should be unchanged')

    def test_DeletingExistingProduct_RemovesItFromTheList(self):
        create_response = self._create_product(self._products['valid'])
        response = self._api.delete(create_response['id'])

        products = self._api.list()
        list_product = self._find_product(products, create_response['id'])

        self.assertEqual(
                response['status'], 1, 'response status should be 1')
        self.assertIsNone(list_product, 'product should be deleted')

    def test_DeletingNonExistingProduct_ReturnsError(self):
        response = self._api.delete(13371488)

        self.assertEqual(response['status'], 0, 'response status should be 0')

    def test_DeletingWithInvalidId_ReturnsError(self):
        response = self._api.delete('whatever')

        self.assertEqual(response['status'], 0, 'response status should be 0')

    def _load_config_json(self, file_path):
        full_path = path.join(self._CONFIG_DIR, file_path)
        with open(full_path, encoding='utf-8') as f:
            return json.loads(f.read())

    def _json_matches_schema(self, data, schema):
        try:
            jsonschema.validate(data, schema)
            return True
        except:
            return False

    def _create_product(self, body):
        response = self._api.add(body)
        if 'id' in response:
            self._created_product_ids.append(response['id'])

        return response

    def _find_product(self, products, id):
        for product in products:
            if int(product['id']) == id:
                return product

        return None

    def test_AddingProduct_InvalidCategory_ReturnsError(self):
        invalid_product = {
            "category_id": "0",
            "title": "Valid Title",
            "alias": "valid-title",
            "content": "Valid Content",
            "price": "100",
            "old_price": "120",
            "status": "1",
            "keywords": "Valid Keywords",
            "description": "Valid Description",
            "hit": "1"
        }

        response = self._api.add(invalid_product)

        self.assertEqual(response['status'], 1, 'response status should be 1')

    def test_AddingProduct_InvalidId_ReturnsError(self):
        invalid_product = {
            "id": "-1",  # invalid id
            "category_id": "1",
            "title": "Valid Title",
            "alias": "valid-title",
            "content": "Valid Content",
            "price": "100",
            "old_price": "120",
            "status": "1",
            "keywords": "Valid Keywords",
            "description": "Valid Description",
            "hit": "1"
        }

        response = self._api.add(invalid_product)

        self.assertEqual(response['status'], 1, 'response status should be 1')

    def test_AddingProduct_InvalidPrice_ReturnsError(self):
        invalid_product = {
            "category_id": "1",
            "title": "Valid Title",
            "alias": "valid-title",
            "content": "Valid Content",
            "price": "-100",  # invalid price
            "old_price": "120",
            "status": "1",
            "keywords": "Valid Keywords",
            "description": "Valid Description",
            "hit": "1"
        }

        response = self._api.add(invalid_product)

        self.assertEqual(response['status'], 1, 'response status should be 1')

    def test_AddingProduct_InvalidStatus_ReturnsError(self):
        invalid_product = {
            "category_id": "1",
            "title": "Valid Title",
            "alias": "valid-title",
            "content": "Valid Content",
            "price": "100",
            "old_price": "120",
            "status": "2",  # invalid status
            "keywords": "Valid Keywords",
            "description": "Valid Description",
            "hit": "1"
        }

        response = self._api.add(invalid_product)

        self.assertEqual(response['status'], 1, 'response status should be 1')

    def test_AddingProduct_InvalidHit_ReturnsError(self):
        invalid_product = {
            "category_id": "1",
            "title": "Valid Title",
            "alias": "valid-title",
            "content": "Valid Content",
            "price": "100",
            "old_price": "120",
            "status": "1",
            "keywords": "Valid Keywords",
            "description": "Valid Description",
            "hit": "2"  # invalid hit
        }

        response = self._api.add(invalid_product)

        self.assertEqual(response['status'], 1, 'response status should be 1')

    def test_AddingProduct_ValidCategory15_Succeeds(self):
        valid_product = {
            "category_id": "15",
            "title": "Valid Title",
            "alias": "valid-title",
            "content": "Valid Content",
            "price": "100",
            "old_price": "120",
            "status": "1",
            "keywords": "Valid Keywords",
            "description": "Valid Description",
            "hit": "1"
        }

        response = self._api.add(valid_product)

        self.assertEqual(response['status'], 1, 'response status should be 1')

    def test_AddingProduct_InvalidCategory16_ReturnsError(self):
        invalid_product = {
            "category_id": "16",  # invalid id
            "title": "Valid Title",
            "alias": "valid-title",
            "content": "Valid Content",
            "price": "100",
            "old_price": "120",
            "status": "1",
            "keywords": "Valid Keywords",
            "description": "Valid Description",
            "hit": "1"
        }

        response = self._api.add(invalid_product)

        self.assertEqual(response['status'], 1, 'response status should be 1')

if __name__ == '__main__':
    unittest.main()