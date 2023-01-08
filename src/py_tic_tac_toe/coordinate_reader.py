from py_tic_tac_toe.board import Board
from re import match

OCCUPIED = 'This cell is occupied! Choose another one!'
INVALID_FORMAT = 'You should enter numbers!'
RANGE_ERROR = 'Coordinates should be from 1 to 3!'


def prompt_for_move(board: Board) -> (int, int):
    while True:
        coord_input = input()
        if not match('-?\\d+\\s+-?\\d+', coord_input):
            print(INVALID_FORMAT)
            continue
        if not match('[123]\\s+[123]', coord_input):
            print(RANGE_ERROR)
            continue
        coords = tuple(int(c) for c in coord_input.split())
        if board.get_cell(coords) in ('X', 'O'):
            print(OCCUPIED)
            continue
        return coords
