"""
The code of the test MUST be commented indicating what are you testing in each
case. For each model the test script should, at least:
    - Create a new instance of the model
    - Retrieve an existing instance of the model (recommended trying with
      different filter options)
    - Update an existing model instance (if update operation is supported by
      this model)
    - Remove an existing model from the database
    - Test that onModify and onDelete work as expected
    - Test possible errors conditions (e.g. foreign keys violation or other
      situation where Integrity error might be raised)
"""
import pytest

from core.models import User

pytestmark = [pytest.mark.django_db, pytest.mark.models]


def test_create_user():
    """Create user with valid values"""
    user = User.objects.create_user(
        username='test',
        password='test123'
    )
    assert str(user) == user.username


def test_get_users_sorted_by_stats():
    """Sort users by win count"""
    user1 = User.objects.create_user(
        username='test',
        password='test123',
        wins=1
    )
    user2 = User.objects.create_user(
        username='test2',
        password='test123',
        wins=5
    )
    users = User.objects.all().order_by("-wins")
    assert users[0] == user2
    assert users[1] == user1


def test_update_user_stats():
    """Update user win count after win"""
    user1 = User.objects.create_user(
        username='test',
        password='test123',
        wins=1
    )

    user1.wins = 2
    user1.save()
    user1.refresh_from_db()
    assert user1.wins == 2


def test_delete_user():
    """Delete user"""
    user = User.objects.create_user(
        username='test',
        password='test123',
    )
    user.delete()
