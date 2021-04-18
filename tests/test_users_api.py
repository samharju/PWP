import json

import pytest
from django.contrib.auth import get_user_model
from rest_framework import status

from rest_framework.reverse import reverse

pytestmark = [pytest.mark.django_db]


def test_create_token(api_client):
    """Retrieve token from token endpoint"""
    user = get_user_model().objects.create_user(
        username='dummy', password='dummy'
    )
    response = api_client.post(
        reverse('users:token'),
        data={
            'username': 'dummy',
            'password': 'dummy'
        }
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['token'] == user.auth_token.key


def test_anon_create_user(api_client):
    """Unathorized user can create new user"""
    response = api_client.post(
        reverse('users:user-list'), data={'username': 'test', 'password': 'test123'}
    )
    print(json.dumps(response.json(), indent=2))
    assert response.status_code == status.HTTP_201_CREATED
