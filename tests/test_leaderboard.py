import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from core.models import User


pytestmark = [pytest.mark.django_db]


def test_leaderboard(authenticate, dummy_user, api_client):

    user2 = User.objects.create_user(
        username='l1',
        password="l11",
        win_percentage=0.20,
        wins=20,
        losses=100
    )
    user1 = User.objects.create_user(
        username='l3',
        password="l33",
        win_percentage=0.30,
        wins=30,
        losses=100
    )
    user3 = User.objects.create_user(
        username='l2',
        password="l22",
        win_percentage=0.10,
        wins=1,
        losses=10
    )
    # unauthenticated
    response = api_client.get(reverse('leaderboard:user-list'))
    data = response.json()
    assert data['items'][1]["username"] == user2.username

    # authenticated
    client = authenticate(dummy_user)
    response = client.get(reverse('leaderboard:user-list'))
    users = User.objects.all().order_by("-win_percentage")
    data = response.json()
    assert users[0] == user1
    assert data['items'][0]["username"] == user1.username
    assert data['items'][1]["wins"] == user2.wins
    assert data['items'][2]["losses"] == user3.losses
    assert len(data['items']) == 4
    assert response.status_code == status.HTTP_200_OK
