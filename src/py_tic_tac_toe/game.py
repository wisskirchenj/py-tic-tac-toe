from py_tic_tac_toe.board import Board
from py_tic_tac_toe.coordinate_reader import prompt_for_move

LINE = '-' * 9


def print_board(board: Board):
    print(LINE)
    for i in range(3):
        print(f'| {" ".join(board.row(i))} |')
    print(LINE)


def main():
    board = Board(input())
    print_board(board)
    coords = prompt_for_move(board)
    board.set_cell(coords, 'X')
    print_board(board)


if __name__ == '__main__':
    main()
