import pytest
from rest_framework.test import APITestCase
from django.shortcuts import reverse
from config_test import EVERYTHING_EQUALS_NOT_NONE


pytestmark = [pytest.mark.django_db]


class TestGuessEndpoints(APITestCase):

    fixtures = ['catalog/tests/fixtures/category_fixtures.json']

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