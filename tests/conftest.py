import pytest

from core.models import Rule
from django.contrib.auth import get_user_model


@pytest.fixture()
def dummy_user():
    return get_user_model().objects.create_user(username='dummy', password='dummy')


@pytest.fixture()
def create_user():
    def create(name, passwd='pass123'):
        return get_user_model().objects.create_user(username=name, password=passwd)
    return create


@pytest.fixture()
def dummy_rule(dummy_user):
    instance, _created = Rule.objects.get_or_create(
        name="tester",
        rows=3,
        columns=3,
        winning_tick_count=3,
        author=dummy_user
    )
    return instance


@pytest.fixture()
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture()
def authenticate(api_client, dummy_user):
    def auth_user(user=dummy_user):
        api_client.force_authenticate(user=user)
        return api_client
    return auth_user
