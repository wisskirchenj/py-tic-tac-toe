import unittest
import py_tic_tac_toe.game as game
from unittest.mock import patch
from io import StringIO


class TestGame(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_example1(self, mock_stdout, mock_input):
        mock_args = ['X_X_O____', '3 1']
        mock_input.side_effect = mock_args
        game.main()
        assert mock_stdout.getvalue() == '''---------
| X _ X |
| _ O _ |
| _ _ _ |
---------
---------
| X _ X |
| _ O _ |
| X _ _ |
---------
'''

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_example2(self, mock_stdout, mock_input):
        mock_args = ['_XXOO_OX_', '1 1']
        mock_input.side_effect = mock_args
        game.main()
        assert mock_stdout.getvalue() == '''---------
| _ X X |
| O O _ |
| O X _ |
---------
---------
| X X X |
| O O _ |
| O X _ |
---------
'''

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_example3(self, mock_stdout, mock_input):
        mock_args = ['_XXOO_OX_', '3 3']
        mock_input.side_effect = mock_args
        game.main()
        assert mock_stdout.getvalue() == '''---------
| _ X X |
| O O _ |
| O X _ |
---------
---------
| _ X X |
| O O _ |
| O X X |
---------
'''

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_example4(self, mock_stdout, mock_input):
        mock_args = ['_XXOO_OX_', '2 3']
        mock_input.side_effect = mock_args
        game.main()
        assert mock_stdout.getvalue() == '''---------
| _ X X |
| O O _ |
| O X _ |
---------
---------
| _ X X |
| O O X |
| O X _ |
---------
'''

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_example5(self, mock_stdout, mock_input):
        mock_args = ['_XXOO_OX_', '3 1', '1 1']
        mock_input.side_effect = mock_args
        game.main()
        assert mock_stdout.getvalue() == '''---------
| _ X X |
| O O _ |
| O X _ |
---------
This cell is occupied! Choose another one!
---------
| X X X |
| O O _ |
| O X _ |
---------
'''

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_example6(self, mock_stdout, mock_input):
        mock_args = ['_XXOO_OX_', 'one', 'one one', '1 1']
        mock_input.side_effect = mock_args
        game.main()
        assert mock_stdout.getvalue() == '''---------
| _ X X |
| O O _ |
| O X _ |
---------
You should enter numbers!
You should enter numbers!
---------
| X X X |
| O O _ |
| O X _ |
---------
'''

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_example7(self, mock_stdout, mock_input):
        mock_args = ['_XXOO_OX_', '4 1', '1 4', '1 1']
        mock_input.side_effect = mock_args
        game.main()
        assert mock_stdout.getvalue() == '''---------
| _ X X |
| O O _ |
| O X _ |
---------
Coordinates should be from 1 to 3!
Coordinates should be from 1 to 3!
---------
| X X X |
| O O _ |
| O X _ |
---------
'''