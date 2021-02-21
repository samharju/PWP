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


def test_game_duplicate_user_not_allowed(dummy_user):
    """Same player can not be used twice for a game instance."""
    with pytest.raises():
        Game.objects.create(
            player1=dummy_user,
            player2=dummy_user
        )
