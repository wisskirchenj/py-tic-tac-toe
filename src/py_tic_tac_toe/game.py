from py_tic_tac_toe.board import Board, UNFINISHED
from py_tic_tac_toe.coordinate_reader import prompt_for_move

LINE = '-' * 9


def print_board(board: Board):
    print(LINE)
    for i in range(3):
        print(f'| {" ".join(board.row(i))} |')
    print(LINE)


def init_board_and_player() -> (Board, str):
    board = Board('_' * 9)
    print_board(board)
    player = 'X'
    return board, player


def toggle_player(player: str):
    return 'O' if player == 'X' else 'X'


def do_next_move(board, player):
    coords = prompt_for_move(board)
    board.set_cell(coords, player)
    print_board(board)


def main():
    board, player = init_board_and_player()
    while board.state() == UNFINISHED:
        do_next_move(board, player)
        player = toggle_player(player)
    print(board.state())


def main_stage4():
    board = Board(input())
    print_board(board)
    coords = prompt_for_move(board)
    board.set_cell(coords, 'X')
    print_board(board)


if __name__ == '__main__':
    main()
