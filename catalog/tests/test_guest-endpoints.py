import pytest
from rest_framework.test import APITestCase
from django.shortcuts import reverse
from config_test import EVERYTHING_EQUALS_NOT_NONE


pytestmark = [pytest.mark.django_db]


class TestGuessEndpoints(APITestCase):

    fixtures = ['catalog/tests/fixtures/category_fixtures.json', 'catalog/tests/fixtures/discount_fixtures.json',
                'catalog/tests/fixtures/product_fixtures.json', 'catalog/tests/fixtures/seller_fixtures.json']

    def test_categories_list_endpoints(self):
        url = reverse('categories')
        response = self.client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 2,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE
            }
        ]

    def test_sellers(self):
        url = reverse('sellers')
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "contact": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 2,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "contact": EVERYTHING_EQUALS_NOT_NONE
            },
        ]

    def test_discounts(self):
        url = reverse('discounts')
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "percent": EVERYTHING_EQUALS_NOT_NONE,
            },
        ]

    def test_category_products(self):
        category_id = 1
        url = reverse('category-products', kwargs={"category_id": category_id})
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == [
            {'id': 1,
             'article': EVERYTHING_EQUALS_NOT_NONE,
             'name': EVERYTHING_EQUALS_NOT_NONE,
             'price': EVERYTHING_EQUALS_NOT_NONE,
             'images': EVERYTHING_EQUALS_NOT_NONE
             }
        ]
