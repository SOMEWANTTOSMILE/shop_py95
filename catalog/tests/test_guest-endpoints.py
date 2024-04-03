import pytest
from rest_framework.test import APITestCase


pytestmark = [pytest.mark.django_db]


class TestGuessEndpoints(APITestCase):
    def test_something(self):
        assert True == True
