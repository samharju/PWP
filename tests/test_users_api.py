import jsonschema
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
    """Unauthorized user can create new user"""
    response = api_client.post(
        reverse('users:user-list'), data={'username': 'test', 'password': 'test123'}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert reverse('users:user-detail', args=('test',)) in response.headers['Location']


def test_user_collection(api_client, create_user):
    """All existing users listed and collection controls present"""
    pate = create_user('pate')
    esa = create_user('esa')
    api_client.force_authenticate(pate)
    res = api_client.get(reverse('users:user-list'))
    data = res.json()

    assert res.status_code == status.HTTP_200_OK
    assert len(data['items']) == 2
    assert pate.username == data['items'][0]['username']
    assert esa.username == data['items'][1]['username']
    assert 'up' in data['@controls']
    assert 'create' in data['@controls']
    assert 'self' in data['items'][0]['@controls']
    assert 'self' in data['items'][1]['@controls']


def test_user_item(authenticate, create_user, dummy_user):
    """User owner details with all controls"""
    pate = create_user('pate')
    client = authenticate(pate)

    public = ['self', 'collection', 'history', 'rules-created']
    private = ['edit', 'delete']

    res = client.get(reverse('users:user-detail', args=(dummy_user.username,)))
    assert res.status_code == status.HTTP_200_OK
    public_data = res.json()
    assert list(public_data['@controls'].keys()) == public

    client = authenticate(dummy_user)
    res = client.get(reverse('users:user-detail', args=(dummy_user.username,)))
    assert res.status_code == status.HTTP_200_OK
    private_data = res.json()
    assert list(private_data['@controls'].keys()) == [*public, *private]


def test_user_update(authenticate, dummy_user):
    """Update user info"""
    client = authenticate()
    res = client.get(
        reverse('users:user-detail', args=(dummy_user.username,))
    )
    controls = res.json()['@controls']
    url = controls['edit']['href']
    method = controls['edit']['method']
    schema = controls['edit']['schema']

    payload = {'password': 'ykskaks'}
    jsonschema.validate(payload, schema)
    res = getattr(client, method.lower())(url, data=payload)
    assert res.status_code == status.HTTP_204_NO_CONTENT

    client.logout()
    res = client.post(
        reverse('users:token'),
        data={'username': dummy_user.username, 'password': 'ykskaks'}
    )
    assert res.status_code == status.HTTP_200_OK
