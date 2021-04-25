import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from core.models import User

pytestmark = [pytest.mark.django_db]


def test_leaderboard(authenticate, dummy_user):

    User.objects.create_user(
        username='l1',
        password="l11",
        win_percentage=0.20,
        wins=20,
        losses=100
    )
    user = User.objects.create_user(
        username='l3',
        password="l33",
        win_percentage=0.30,
        wins=30,
        losses=100
    )
    # get_user_model().objects.create_user(
    User.objects.create_user(
        username='l2',
        password="l22",
        win_percentage=0.10,
        wins=1,
        losses=10
    )
    client = authenticate(dummy_user)
    response = client.get(reverse('leaderboard:user-list'))
    users = User.objects.all().order_by("-win_percentage")
    assert users[0] == user
    assert response.status_code == status.HTTP_200_OK
