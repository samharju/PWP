import itertools
from collections import namedtuple

from core.models import Rule

Move = namedtuple('Move', ['row', 'column', 'marker'])


def str_to_arrays(rule: Rule, board: str):
    """Build list of lists."""
    char_list = [char for char in board]
    array = []
    for i in range(rule.rows):
        row = []
        array.append(row)
        for j in range(rule.columns):
            row.append(char_list.pop(0))
    return array


def arrays_to_str(board: list[list]):
    """Concatenate list of list to one string."""
    return "".join([str(x) for x in list(itertools.chain(*board))])


def add_move_if_ok(board: list[list], new_move: Move) -> (bool, str):
    """
    Add player mark on board.

    :param board: list of lists illustrating game board
    :param new_move: Move-object with zero based coords and marker letter
    :return: success, error message
    """
    try:
        if not board[new_move.row][new_move.column] == ' ':
            return False, 'Select empty slot on board'
        board[new_move.row][new_move.column] = new_move.marker
        return True, ''
    except IndexError:
        return False, 'Move was out of bounds'


def is_winning_move(rule: Rule, board: list[list], new_move: Move) -> bool:
    """Check row, column and diagonals of last added move."""
    return any([
        _check_row_and_column(rule, board, new_move),
        _check_diags(rule, board, new_move)
    ])


def _check_row_and_column(rule: Rule, board, new_move: Move):
    board[new_move.row][new_move.column] = new_move.marker
    new_row = "".join(board[new_move.row])
    new_col = "".join([row[new_move.column] for row in board])

    return any([
        rule.winning_tick_count * new_move.marker in new_row,
        rule.winning_tick_count * new_move.marker in new_col
    ])


def _check_diags(rule: Rule, board, new_move: Move):

    left = []
    """Check southwest
    _ _ _ _ _
    _ _ _ _ _
    _ _ X _ _
    _ x _ _ _
    x _ _ _ _
    """
    current_col = new_move.column
    current_row = new_move.row

    while 0 <= current_col and current_row < rule.rows:
        left.insert(0, board[current_row][current_col])
        current_col -= 1
        current_row += 1

    if rule.winning_tick_count * new_move.marker in "".join(left):
        return True

    """Check northeast
    _ _ _ _ x
    _ _ _ x _
    _ _ X _ _
    _ x _ _ _
    x _ _ _ _
    """
    current_col = new_move.column
    current_row = new_move.row

    while current_col < rule.columns and 0 <= current_row:
        left.append(board[current_row][current_col])
        current_col += 1
        current_row -= 1

    if rule.winning_tick_count * new_move.marker in "".join(left):
        return True

    right = []
    """Check northwest
    x _ _ _ _
    _ x _ _ _
    _ _ X _ _
    _ _ _ _ _
    _ _ _ _ _
    """
    current_col = new_move.column
    current_row = new_move.row

    while 0 <= current_col and 0 <= current_row:
        right.insert(0, board[current_row][current_col])
        current_col -= 1
        current_row -= 1

    if rule.winning_tick_count * new_move.marker in "".join(right):
        return True

    """Check southeast
    x _ _ _ _
    _ x _ _ _
    _ _ X _ _
    _ _ _ x _
    _ _ _ _ x
    """
    current_col = new_move.column
    current_row = new_move.row
    while current_col < rule.columns and current_row < rule.rows:
        right.append(board[current_row][current_col])
        current_col += 1
        current_row += 1

    if rule.winning_tick_count * new_move.marker in "".join(right):
        return True
    return False
