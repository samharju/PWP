from rest_framework import status
from rest_framework.reverse import reverse

import pytest

pytestmark = [pytest.mark.django_db, pytest.mark.models]

resources = [
    reverse('users:user-list'),
    reverse('users:user-detail', args=('123',)),
    reverse('rules:rule-list'),
    reverse('rules:rule-detail', args=('456',)),
    reverse('games:game-list'),
    reverse('games:game-detail', args=('789',)),
]


@pytest.mark.parametrize('method', ['get', 'post', 'put', 'delete'])
@pytest.mark.parametrize('endpoint', resources)
def test_auth_required(api_client, endpoint, method):
    """Authentication generally required"""
    if endpoint == reverse('users:user-list') and method == 'post':
        return
    response = api_client.__getattribute__(method)(endpoint)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_auth_not_required(api_client):
    """Leaderboard, user creation and token retrieval does not require auth header."""
    response = api_client.post(reverse('users:user-list'))
    assert response.status_code != status.HTTP_401_UNAUTHORIZED

    response = api_client.post(reverse('leaderboard:user-list'))
    assert response.status_code != status.HTTP_401_UNAUTHORIZED

    response = api_client.post(reverse('users:token'))
    assert response.status_code != status.HTTP_401_UNAUTHORIZED
