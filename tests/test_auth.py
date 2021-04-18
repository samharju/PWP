from rest_framework import status
from rest_framework.reverse import reverse

import pytest


resources = [
    reverse('users:user-list'),
    reverse('users:user-detail', args=('placeholder',)),
    reverse('rules:rule-list'),
    reverse('rules:rule-detail', args=('placeholder',)),

]


@pytest.mark.parametrize('method', ['get', 'post', 'put', 'delete'])
@pytest.mark.parametrize('endpoint', resources)
def test_auth_required(api_client, endpoint, method):
    """Authentication required for """
    if endpoint == reverse('users:user-list') and method == 'post':
        return
    response = api_client.__getattribute__(method)(endpoint)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
