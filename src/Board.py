from BigCell import *


class Board:
    def __init__(self, width, height):
        self.current_player = PLAYER_1
        self.columns = width
        self.rows = height
        self.cells = width * [None]
        for x in range(0, width):
            column = height * [None]
            self.cells[x] = column
            for y in range(0, height):
                column[y] = BigCell(x, y, width, height)

    def get_current_player(self):
        return self.current_player

    def get_cell(self, col, row) -> BigCell:
        return self.cells[col][row]

    def get_columns(self):
        return self.columns

    def get_rows(self):
        return self.rows
