import BigCell


class Board:
    def __init__(self, width, height):
        self.cells = width * [None]
        for x in range(0, width):
            column = height * [None]
            self.cells[x] = column
            for y in range(0, height):
                column[y] = BigCell.BigCell(x, y, width, height)

    def get_cell(self, x, y):
        return self.cells[x][y]
