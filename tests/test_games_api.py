import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from core.models import Game

pytestmark = [pytest.mark.django_db]


def test_create_game(authenticate, dummy_user, dummy_rule):
    user = dummy_user
    client = authenticate(user)

    response = client.post(
        reverse('games:game-list'),
        data={'rule': dummy_rule.name}
    )
    game = Game.objects.first()
    assert game.player1 == user
    assert len(game.board) == dummy_rule.rows * dummy_rule.columns
    assert response.status_code == status.HTTP_201_CREATED
    assert reverse('games:game-detail', args=(game.id,)) in response.headers['Location']


def test_game_collection(authenticate, dummy_user, dummy_rule):
    client = authenticate(dummy_user)
    client.post(reverse('games:game-list'), data={'rule': dummy_rule.name})
    client.post(reverse('games:game-list'), data={'rule': dummy_rule.name})
    response = client.get(reverse('games:game-list'))
    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert "create" in data['@controls']
    assert "up" in data['@controls']
    assert len(data['items']) == 2


def test_join_game(authenticate, create_user, dummy_rule):
    """Create game as pate, join game as esa utilizing only controls from responses."""

    # Init users, create game as pate
    pate = create_user('pate')
    esa = create_user('esa')
    client = authenticate(pate)
    client.post(reverse('games:game-list'), data={'rule': dummy_rule.name})

    # Switch to esa, join game using controls
    client.force_authenticate(esa)
    entrypoint = client.get('/api/').json()
    game_control = entrypoint['@controls']['games']['href']
    collection = client.get(game_control).json()
    game_item = client.get(collection['items'][0]['@controls']['self']['href']).json()
    game_join_control = game_item['@controls']['join']
    response = getattr(client, game_join_control['method'].lower())(
        game_join_control['href']
    )
    assert response.status_code == status.HTTP_200_OK


def test_add_move_and_win(authenticate, create_user, dummy_rule):
    pate = create_user('pate')
    esa = create_user('esa')
    client = authenticate(pate)

    game = Game.objects.create(
        player1=pate,
        player2=esa,
        rule=dummy_rule,
        board=' X OX O  ',
        turn=2
    )
    res = client.put(
        reverse('games:game-add-move', args=(game.id,)),
        data={'row': 2, 'column': 1}
    )
    assert res.status_code == status.HTTP_204_NO_CONTENT

    res = client.get(reverse('games:game-detail', args=(game.id,)))
    print(res.json())

    pate.refresh_from_db()
    esa.refresh_from_db()

    assert pate.wins == 1
    assert pate.win_percentage == 1
    assert esa.win_percentage == 0
    assert esa.losses == 1
