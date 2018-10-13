import unittest

import BigCell
import Board
from BigCell import BigCell

class BoardTest(unittest.TestCase):

    def test_top_left_corner(self):
        board = Board.Board(4, 3)
        top_left = self.check_cell(board, 0, 0)
        self.assertEqual(True, top_left.has_bottom())
        self.assertEqual(True, top_left.has_right())
        self.assertEqual(False, top_left.has_left())
        self.assertEqual(False, top_left.has_top())

    def test_another_cell(self):
        board = Board.Board(24, 53)
        self.check_cell(board, 14, 32)

    def check_cell(self, board, x, y) -> BigCell:
        result = board.get_cell(x, y)
        self.assertEqual(x, result.get_x())
        self.assertEqual(y, result.get_y())
        return result
