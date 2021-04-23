import pytest

from core.models import Rule
from games.tictactoe import (
    Move, _check_diags, _check_row_and_column, add_move_if_ok, is_winning_move,
    str_to_arrays,
)

pytestmark = [pytest.mark.django_db]


@pytest.fixture()
def rule3x3x3(dummy_user):
    return Rule.objects.create(
        name='test',
        author=dummy_user
    )


@pytest.fixture()
def rule5x5x3(dummy_user):
    return Rule.objects.create(
        name='test2',
        rows=5,
        columns=5,
        winning_tick_count=3,
        author=dummy_user
    )


def test_add_move_if_ok():
    state = [
        [' ', 'O', ' '],
        ['X', 'X', ' '],
        ['O', 'O', ' ']
    ]
    new = Move(1, 1, 'X')
    ok, error = add_move_if_ok(state, new)
    assert not ok
    assert error

    new = Move(1, 2, 'X')
    ok, _ = add_move_if_ok(state, new)
    assert ok
    assert state[1][2] == 'X'

    new = Move(52, -5, 'X')
    ok, _ = add_move_if_ok(state, new)
    assert not ok


def test_is_winning_move(rule3x3x3):
    state = [
        [' ', 'O', ' '],
        ['X', 'X', ' '],
        ['O', 'O', ' ']
    ]
    new = Move(1, 2, 'X')
    add_move_if_ok(state, new)
    assert is_winning_move(rule3x3x3, state, new)

    state = [
        [' ', 'O', ' '],
        ['X', 'X', ' '],
        ['O', 'O', ' ']
    ]
    new = Move(1, 2, 'X')
    add_move_if_ok(state, new)
    assert is_winning_move(rule3x3x3, state, new)


def test_str_to_array(rule3x3x3):
    state = [
        [' ', 'O', ' '],
        ['X', 'X', ' '],
        ['O', 'O', ' ']
    ]
    assert str_to_arrays(rule3x3x3, ' O XX OO ') == state


def test_check_row(rule3x3x3):
    state = [
        [' ', 'O', ' '],
        ['X', 'X', ' '],
        ['O', 'O', ' ']
    ]
    new = Move(1, 2, 'X')
    add_move_if_ok(state, new)
    assert _check_row_and_column(rule3x3x3, state, new)


def test_check_col(rule3x3x3):
    state = [
        [' ', ' ', ' '],
        ['X', 'O', ' '],
        ['X', 'O', ' ']
    ]
    new = Move(0, 1, 'O')
    add_move_if_ok(state, new)
    assert _check_row_and_column(rule3x3x3, state, new)


def test_check_diag(rule3x3x3, rule5x5x3):
    state = str_to_arrays(rule3x3x3, 'O  XO X  ')
    new = Move(2, 2, 'O')
    add_move_if_ok(state, new)
    assert _check_diags(rule3x3x3, state, new)

    state = str_to_arrays(rule3x3x3, 'O  OX X  ')
    new = Move(0, 2, 'X')
    add_move_if_ok(state, new)
    assert _check_diags(rule3x3x3, state, new)

    state = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', 'O', ' ', ' ', ' '],
        [' ', ' ', 'O', ' ', ' '],
        [' ', ' ', ' ', 'X', ' '],
        [' ', ' ', 'X', ' ', ' ']
    ]
    new = Move(2, 4, 'X')
    add_move_if_ok(state, new)
    assert _check_diags(rule5x5x3, state, new)

    new = Move(0, 0, 'O')
    add_move_if_ok(state, new)
    assert _check_diags(rule5x5x3, state, new)
