import pytest
from rest_framework import status

from rest_framework.reverse import reverse

from core.models import Rule

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
