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
from django.db.models import ProtectedError

from core.models import Game, Rule

pytestmark = [pytest.mark.django_db, pytest.mark.models]


def test_create_rules(dummy_user):
    """Create rules instance with valid input."""
    rules = Rule.objects.create(
        name="test-create",
        rows=5,
        columns=5,
        winning_tick_count=5,
        author=dummy_user
    )
    assert rules.name == "test-create"


faulty_rules = [
    {
        "name": "faulty_rows1",
        "rows": 2,
        "columns": 3,
        "winning_tick_count": 3
    },
    {
        "name": "faulty_rows2",
        "rows": 11,
        "columns": 3,
        "winning_tick_count": 3
    },
    {
        "name": "faulty_cols1",
        "rows": 3,
        "columns": 2,
        "winning_tick_count": 3
    },
    {
        "name": "faulty_cols2",
        "rows": 3,
        "columns": 11,
        "winning_tick_count": 3
    },
    {
        "name": "faulty_win1",
        "rows": 5,
        "columns": 5,
        "winning_tick_count": 2
    },
    {
        "name": "faulty_win1",
        "rows": 10,
        "columns": 10,
        "winning_tick_count": 11
    }
]


@pytest.mark.parametrize("test_input", faulty_rules)
def test_rules_validation(test_input, dummy_user):
    """Each rule property must be greater than zero."""
    with pytest.raises(ValidationError):
        Rule.objects.create(
            **test_input,
            author=dummy_user
        )


def test_filter_rules(pate_and_esa):
    """Rules filtered by author."""
    pate, esa = pate_and_esa
    rule1 = Rule.objects.create(
        name='test1',
        rows=3,
        columns=3,
        winning_tick_count=3,
        author=pate
    )
    Rule.objects.create(
        name='test2',
        rows=3,
        columns=3,
        winning_tick_count=3,
        author=esa
    )

    rules = Rule.objects.filter(author=pate)
    assert len(rules) == 1
    assert rules[0] == rule1


def test_delete_rule_not_yet_assigned(dummy_user):
    """Rule is protected on game model, thus delete allowed only when no relations
    have been created.
    """
    rule = Rule.objects.create(
        name='test1',
        rows=3,
        columns=3,
        winning_tick_count=3,
        author=dummy_user
    )
    assert len(Rule.objects.all()) == 1

    rule.delete()
    assert len(Rule.objects.all()) == 0

    rule = Rule.objects.create(
        name='test1',
        rows=3,
        columns=3,
        winning_tick_count=3,
        author=dummy_user
    )

    Game.objects.create(
        player1=dummy_user,
        rule=rule
    )

    with pytest.raises(ProtectedError):
        rule.delete()

    assert len(Rule.objects.all()) == 1
