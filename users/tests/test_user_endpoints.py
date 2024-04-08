import pytest
from rest_framework.test import APITestCase, APIClient
from django.shortcuts import reverse
from config_test import EVERYTHING_EQUALS_NOT_NONE
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


pytestmark = [pytest.mark.django_db]


class LoginTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        password = make_password('t8u39tg8904!')

        self.user = get_user_model().objects.create(
            email='test1@gmail.com',
            password=password,
            is_active=True
        )

        data = {
            "email": 'test1@gmail.com',
            "password": 't8u39tg8904!'
        }

        url = reverse('jwt-create')

        self.token = 'Bearer ' + self.client.post(
            url,
            data=data,
            format='json'
        ).data['access']

    def test_login(self):
        url = reverse('test-login')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == 'darova'
