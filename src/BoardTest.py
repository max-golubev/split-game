import unittest
import Board
import BigCell

class BoardTest(unittest.TestCase):

    def test_top_left_corner(self):
        board = Board.Board(4, 3)
        top_left = board.get_cell(0, 0)
        self.assertEqual()



