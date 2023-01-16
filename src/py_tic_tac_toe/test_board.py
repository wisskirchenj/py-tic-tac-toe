import unittest

import py_tic_tac_toe.board as boa


# noinspection SpellCheckingInspection
class BoardTest(unittest.TestCase):

    def test_row(self):
        board = boa.Board('XXXOO__O_')
        self.assertListEqual(board.row(0), ['X', 'X', 'X'])
        self.assertListEqual(board.row(1), ['O', 'O', '_'])
        self.assertListEqual(board.row(2), ['_', 'O', '_'])

    def test_column(self):
        board = boa.Board('XXXOO__O_')
        self.assertListEqual(board.column(0), ['X', 'O', '_'])
        self.assertListEqual(board.column(1), ['X', 'O', 'O'])
        self.assertListEqual(board.column(2), ['X', '_', '_'])

    def test_diagonal(self):
        board = boa.Board('XXXOO__O_')
        self.assertListEqual(board.diagonal(0), ['X', 'O', '_'])
        self.assertListEqual(board.diagonal(1), ['X', 'O', '_'])

    def test_x_placed_count(self):
        board = boa.Board('XXXOO__O_')
        self.assertEqual(board.x_placed_count(), 3)

    def test_o_placed_count(self):
        board = boa.Board('XXXOO__O_')
        self.assertEqual(board.o_placed_count(), 3)

    def test_has_triple(self):
        board = boa.Board('XXXOO__O_')
        self.assertTrue(board.has_triple({'X'}))
        self.assertFalse(board.has_triple({'O'}))
        board = boa.Board('XOX_OX_OX')
        self.assertTrue(board.has_triple({'X'}))
        self.assertTrue(board.has_triple({'O'}))
        board = boa.Board('X_O_XO_OX')
        self.assertTrue(board.has_triple({'X'}))
        self.assertFalse(board.has_triple({'O'}))

    def test_state(self):
        board = boa.Board('X_O_XO_OX')
        self.assertEqual(board.state(), boa.X_WINS)
        board = boa.Board('XOXOXOXXO')
        self.assertEqual(board.state(), boa.X_WINS)
        board = boa.Board('XOOOXOXXO')
        self.assertEqual(board.state(), boa.O_WINS)
        board = boa.Board('XOXOOXXXO')
        self.assertEqual(board.state(), boa.DRAW)
        board = boa.Board('XO_OOX_X_')
        self.assertEqual(board.state(), boa.UNFINISHED)
        board = boa.Board('XO_XO_XOX')
        self.assertEqual(board.state(), boa.IMPOSSIBLE)
        board = boa.Board('_O_X__X_X')
        self.assertEqual(board.state(), boa.IMPOSSIBLE)
        board = boa.Board('_OOOO_X_X')
        self.assertEqual(board.state(), boa.IMPOSSIBLE)


if __name__ == "__main__":
    unittest.main()
