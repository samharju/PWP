import pytest

from core.models import User

pytestmark = pytest.mark.django_db


def test_user_str():
    """User string representation is username."""
    user = User.objects.create_user(
        username='test',
        email='test@test.com',
        password='test123'
    )
    assert str(user) == user.username
