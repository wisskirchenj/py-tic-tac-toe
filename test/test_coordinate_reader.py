import unittest
import py_tic_tac_toe.coordinate_reader as coord
import py_tic_tac_toe.board as board
from unittest.mock import patch
from io import StringIO


class CoordinateReaderTest(unittest.TestCase):

    def setUp(self) -> None:
        self.test_board = board.Board('OO_XXX___')

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_for_move_invalid(self, mock_stdout, mock_input):
        mock_args = ['one one', '1 3']
        mock_input.side_effect = mock_args
        self.assertEqual((1, 3), coord.prompt_for_move(self.test_board))
        assert mock_stdout.getvalue() == coord.INVALID_FORMAT + '\n'

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_for_move_range(self, mock_stdout, mock_input):
        mock_args = ['2 0', '1 3']
        mock_input.side_effect = mock_args
        self.assertEqual((1, 3), coord.prompt_for_move(self.test_board))
        assert mock_stdout.getvalue() == coord.RANGE_ERROR + '\n'

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_for_move_range2(self, mock_stdout, mock_input):
        mock_args = ['4 11', '1 3']
        mock_input.side_effect = mock_args
        self.assertEqual((1, 3), coord.prompt_for_move(self.test_board))
        assert mock_stdout.getvalue() == coord.RANGE_ERROR + '\n'

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_for_move_range3(self, mock_stdout, mock_input):
        mock_args = ['3 -1', '1 3']
        mock_input.side_effect = mock_args
        self.assertEqual((1, 3), coord.prompt_for_move(self.test_board))
        assert mock_stdout.getvalue() == coord.RANGE_ERROR + '\n'

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_for_move_occupied(self, mock_stdout, mock_input):
        mock_args = ['1 1', '1 3']
        mock_input.side_effect = mock_args
        self.assertEqual((1, 3), coord.prompt_for_move(self.test_board))
        assert mock_stdout.getvalue() == coord.OCCUPIED + '\n'

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_for_move_occupied2(self, mock_stdout, mock_input):
        mock_args = ['2 2', '3 3']
        mock_input.side_effect = mock_args
        self.assertEqual((3, 3), coord.prompt_for_move(self.test_board))
        assert mock_stdout.getvalue() == coord.OCCUPIED + '\n'

