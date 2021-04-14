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

from core.models import Rule

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
        "name": "test",
        "rows": 0,
        "columns": 3,
        "winning_tick_count": 3
    },
    {
        "name": "test",
        "rows": 3,
        "columns": 0,
        "winning_tick_count": 3
    },
    {
        "name": "test",
        "rows": 3,
        "columns": 3,
        "winning_tick_count": 0
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
