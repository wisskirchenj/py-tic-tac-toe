from board import Board

LINE = '_' * 9


def print_board(board: Board):
    print(LINE)
    for i in range(3):
        print(f'| {" ".join(board.row(i))} |')
    print(LINE)


def main():
    board = Board(input())
    print_board(board)
    print(board.state())


if __name__ == '__main__':
    main()
