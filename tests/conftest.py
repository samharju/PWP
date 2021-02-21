import pytest

from core.models import User, Rules


@pytest.fixture()
def dummy_user(name="tester"):
    instance, _created = User.objects.get_or_create(username=name)
    return instance


@pytest.fixture()
def dummy_rules():
    instance, _created = Rules.objects.get_or_create(
        name="tester",
        rows=3,
        columns=3,
        winning_tick_count=3
    )
    return instance


@pytest.fixture()
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
