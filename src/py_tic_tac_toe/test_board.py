import unittest

import py_tic_tac_toe.board as sub


class BoardTest(unittest.TestCase):

    def test_row(self):
        board = sub.Board('XXXOO__O_')
        self.assertListEqual(board.row(0), ['X', 'X', 'X'])
        self.assertListEqual(board.row(1), ['O', 'O', '_'])
        self.assertListEqual(board.row(2), ['_', 'O', '_'])

    def test_column(self):
        board = sub.Board('XXXOO__O_')
        self.assertListEqual(board.column(0), ['X', 'O', '_'])
        self.assertListEqual(board.column(1), ['X', 'O', 'O'])
        self.assertListEqual(board.column(2), ['X', '_', '_'])

    def test_diagonal(self):
        board = sub.Board('XXXOO__O_')
        self.assertListEqual(board.diagonal(0), ['X', 'O', '_'])
        self.assertListEqual(board.diagonal(1), ['X', 'O', '_'])

    def test_x_placed_count(self):
        board = sub.Board('XXXOO__O_')
        self.assertEqual(board.x_placed_count(), 3)

    def test_o_placed_count(self):
        board = sub.Board('XXXOO__O_')
        self.assertEqual(board.o_placed_count(), 3)

    def test_has_triple(self):
        board = sub.Board('XXXOO__O_')
        self.assertTrue(board.has_triple({'X'}))
        self.assertFalse(board.has_triple({'O'}))
        board = sub.Board('XOX_OX_OX')
        self.assertTrue(board.has_triple({'X'}))
        self.assertTrue(board.has_triple({'O'}))
        board = sub.Board('X_O_XO_OX')
        self.assertTrue(board.has_triple({'X'}))
        self.assertFalse(board.has_triple({'O'}))

    def test_state(self):
        board = sub.Board('X_O_XO_OX')
        self.assertEqual(board.state(), sub.X_WINS)
        board = sub.Board('XOXOXOXXO')
        self.assertEqual(board.state(), sub.X_WINS)
        board = sub.Board('XOOOXOXXO')
        self.assertEqual(board.state(), sub.O_WINS)
        board = sub.Board('XOXOOXXXO')
        self.assertEqual(board.state(), sub.DRAW)
        board = sub.Board('XO_OOX_X_')
        self.assertEqual(board.state(), sub.UNFINISHED)
        board = sub.Board('XO_XO_XOX')
        self.assertEqual(board.state(), sub.IMPOSSIBLE)
        board = sub.Board('_O_X__X_X')
        self.assertEqual(board.state(), sub.IMPOSSIBLE)
        board = sub.Board('_OOOO_X_X')
        self.assertEqual(board.state(), sub.IMPOSSIBLE)


if __name__ == "__main__":
    unittest.main()
