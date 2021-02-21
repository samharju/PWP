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

from core.models import SoloGame

pytestmark = [pytest.mark.django_db, pytest.mark.models]


@pytest.fixture(scope="module")
def sample_solo_game(dummy_user, dummy_rules):
    return SoloGame.objects.create(
        player=dummy_user,
        rules=dummy_rules
    )


def test_create_solo_game(sample_solo_game):
    """Create a game with valid options"""
    assert sample_solo_game.winner == 0


def test_update_solo_game(sample_solo_game):
    """Update solo game board"""
    sample_solo_game.board = "12345"
    sample_solo_game.save()
    sample_solo_game.refresh_from_db()
    assert sample_solo_game.board == "12345"


def test_delete_solo_game(dummy_user, dummy_rules):
    """Delete solo game"""
    game = SoloGame.objects.create(
        player=dummy_user,
        rules=dummy_rules
    )
    game.delete()
