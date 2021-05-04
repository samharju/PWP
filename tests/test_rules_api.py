import pytest
from rest_framework import status

from rest_framework.reverse import reverse

from core.models import Game, Rule

pytestmark = [pytest.mark.django_db]


def test_rule_collection(authenticate, dummy_user):
    """Rule collection returns all rules"""
    Rule.objects.create(
        name='test1',
        author=dummy_user
    )
    Rule.objects.create(
        name='test2',
        author=dummy_user
    )
    client = authenticate(dummy_user)
    response = client.get(reverse('rules:rule-list'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()['items']) == 2


def test_rule_item(authenticate, create_user, dummy_rule):
    """Only author has full controls"""
    controls = ['self', 'collection', 'author', 'delete']
    client = authenticate()
    res = client.get(reverse('rules:rule-detail', args=(dummy_rule.pk,)))
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert list(data['@controls'].keys()) == controls

    pate = create_user('pate')
    client = authenticate(pate)
    res = client.get(reverse('rules:rule-detail', args=(dummy_rule.pk,)))
    assert 'delete' not in res.json()['@controls']

    res = client.delete(reverse('rules:rule-detail', args=(dummy_rule.pk,)))
    assert res.status_code == status.HTTP_403_FORBIDDEN


def test_create_rule(authenticate, dummy_user):
    """User from request set as author."""
    client = authenticate(dummy_user)
    res = client.post(reverse('rules:rule-list'), data={'name': 'test1'})
    assert res.status_code == status.HTTP_201_CREATED
    assert res.data is None
    assert 'Location' in res.headers
    rule = Rule.objects.get(name='test1')
    assert rule.author == dummy_user


def test_rule_filter_by_author(authenticate, create_user, dummy_rule):
    """Only rules by queried author returned."""
    pate = create_user('pate')
    client = authenticate(pate)
    collection = reverse('rules:rule-list')
    client.post(collection, data={'name': 'test1'})
    client.post(collection, data={'name': 'test2'})
    assert Rule.objects.count() == 3

    res = client.get(reverse('rules:rule-list')+'?author=pate')
    assert res.status_code == status.HTTP_200_OK

    data = res.json()
    assert len(data['items']) == 2
    assert data['items'][0]['author'] == "pate"
    assert data['items'][1]['author'] == "pate"


def test_delete_rule(authenticate, dummy_user):
    """Successful request returns 204.
    Trying to delete protected instance returns 400.
    """
    client = authenticate(dummy_user)
    rule = Rule.objects.create(
        name='test1',
        author=dummy_user
    )

    res = client.delete(reverse('rules:rule-detail', args=(rule.name,)))
    assert res.status_code == status.HTTP_204_NO_CONTENT

    rule = Rule.objects.create(
        name='test1',
        author=dummy_user
    )
    Game.objects.create(
        player1=dummy_user,
        rule=rule
    )

    res = client.delete(reverse('rules:rule-detail', args=(rule.name,)))
    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert '@error' in res.json()
