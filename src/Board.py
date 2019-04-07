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

    def start_next_turn(self):
        self.current_player = self.compute_next_player()
        return self.get_current_player()

    def compute_next_player(self):
        current = self.get_current_player()
        if current == PLAYER_1:
            return PLAYER_2
        if current == PLAYER_2:
            return PLAYER_3
        if current == PLAYER_3:
            return PLAYER_4
        if current == PLAYER_4:
            return PLAYER_1
        raise "Unknown player: " + repr(current)

    def get_cell(self, col, row) -> BigCell:
        return self.cells[col][row]

    def get_columns(self):
        return self.columns

    def get_rows(self):
        return self.rows
