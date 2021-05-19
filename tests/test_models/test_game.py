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
from django.db.models import ProtectedError, Q

from core.models import Game, User

pytestmark = [pytest.mark.django_db, pytest.mark.models]


def test_create_game(dummy_user, dummy_rule):
    """Create game with valid values."""
    game = Game.objects.create(
        player1=dummy_user,
        rule=dummy_rule
    )

    assert game.turn == 0
    assert game.winner == 0


def test_game_duplicate_user_not_allowed(dummy_user, dummy_rule):
    """Same player can not be used twice for a game instance."""
    with pytest.raises(ValidationError):
        Game.objects.create(
            player1=dummy_user,
            player2=dummy_user,
            rule=dummy_rule
        )


def test_get_game_by_player(dummy_rule, pate_and_esa):
    """Filter games by players."""
    pate, esa = pate_and_esa
    game1 = Game.objects.create(
        player1=pate,
        rule=dummy_rule
    )
    Game.objects.create(
        player1=pate,
        player2=esa,
        rule=dummy_rule
    )
    game3 = Game.objects.create(
        player1=esa,
        rule=dummy_rule
    )

    games = Game.objects.filter(Q(player1=pate) | Q(player2=pate))
    assert len(games) == 2
    assert game3 not in games

    games = Game.objects.filter(Q(player1=esa) | Q(player2=esa))
    assert len(games) == 2
    assert game1 not in games


def test_update_game(dummy_user, dummy_rule):
    """Turn is updated to db when edited."""
    game = Game.objects.create(
        player1=dummy_user,
        rule=dummy_rule
    )

    game.turn = 1
    game.save()
    game.refresh_from_db()
    assert game.turn == 1


def test_delete_game(dummy_user, dummy_rule):
    """Deleted game doesnt exist after deleted."""

    game = Game.objects.create(
        player1=dummy_user,
        rule=dummy_rule
    )

    game.delete()

    assert 0 == len(Game.objects.filter(player1=dummy_user))


def test_players_nullable(dummy_rule):
    """If related players are deleted, foreign keys are set to null."""
    pate = User.objects.create_user("pate")
    esa = User.objects.create_user("esa")

    game = Game.objects.create(
        player1=pate,
        player2=esa,
        rule=dummy_rule
    )

    pate.delete()
    esa.delete()

    game.refresh_from_db()
    assert game.player1 is None
    assert game.player2 is None


def test_rule_required(dummy_user, dummy_rule):
    """Rule can not be null."""
    with pytest.raises(ValidationError):
        Game.objects.create(
            player1=dummy_user
        )


def test_rule_protected(dummy_user, dummy_rule):
    """Rule deletion blocked if foreign key relation exists."""
    Game.objects.create(
        player1=dummy_user,
        rule=dummy_rule
    )

    with pytest.raises(ProtectedError):
        dummy_rule.delete()
