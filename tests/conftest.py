import pytest

from core.models import Rule
from django.contrib.auth import get_user_model


@pytest.fixture()
def dummy_user(name='dummy', passwd='dummy'):
    return get_user_model().objects.create_user(username=name, password=passwd)


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
def authenticate(api_client):
    def auth_user(user):
        api_client.force_authenticate(user=user)
        return api_client
    return auth_user
