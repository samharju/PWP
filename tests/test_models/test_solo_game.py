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


def test_create_solo_game(dummy_user, dummy_rules):
    """Create a game with valid options"""
    game = SoloGame.objects.create(
        player=dummy_user,
        rules=dummy_rules
    )

    assert game.winner == 0
