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
from django.core.exceptions import ValidationError

from core.models import Game

pytestmark = [pytest.mark.django_db, pytest.mark.models]


def test_create_game(dummy_user, dummy_rules):
    """Create game with valid values."""
    game = Game.objects.create(
        player1=dummy_user,
        rules=dummy_rules
    )

    assert game.turn == 0
    assert game.winner == 0


def test_game_duplicate_user_not_allowed(dummy_user, dummy_rules):
    """Same player can not be used twice for a game instance."""
    with pytest.raises(ValidationError):
        Game.objects.create(
            player1=dummy_user,
            player2=dummy_user,
            rules=dummy_rules
        )


def test_get_game_by_player(dummy_user, dummy_rules):
    """Filter games by players."""
    Game.objects.create(
        player1=dummy_user,
        rules=dummy_rules
    )

    games = Game.objects.filter(player1=dummy_user)
    assert len(games) == 1
    assert games[0].player1 == dummy_user


def test_update_game(dummy_user, dummy_rules):
    """Turn is updated to db when edited."""
    game = Game.objects.create(
        player1=dummy_user,
        rules=dummy_rules
    )

    game.turn = 1
    game.save()
    game.refresh_from_db()
    assert game.turn == 1


def test_delete_game(dummy_user, dummy_rules):
    """Deleted game doesnt exist after deleted."""

    game = Game.objects.create(
        player1=dummy_user,
        rules=dummy_rules
    )

    game.delete()

    assert 0 == len(Game.objects.filter(player1=dummy_user))
