import Board
import BigCell
import pygame

border_color = (0, 0, 255)
cell_color = (100, 100, 100)

class BoardPainter:
    def __init__(self, cell, small, screen: pygame.Surface):
        self.cell = cell #size in pixels
        self.small = small #pixels
        self.screen = screen
        self.x0, self.y0 = 10, 10

    def draw_board(self, board: Board.Board):
        self.draw_cells(board)
        self.draw_borders(board)

    def draw_cells(self, board: Board.Board):
        for row in range(0, board.get_rows()):
            for col in range(0, board.get_columns()):
                cell = board.get_cell(col, row)
                self.draw_cell(cell, col, row)

    def draw_cell(self, cell: BigCell.BigCell, col, row):
        top = self.cell * row + self.y0
        left = self.cell * col + self.x0
        delta = (self.cell - self.small) / 2
        if cell.has_top():
            self.draw_small_cell(left + delta, top)
        if cell.has_left():
            self.draw_small_cell(left, top + delta)
        if cell.has_bottom():
            self.draw_small_cell(left + delta, top + self.cell - self.small)
        if cell.has_right():
            self.draw_small_cell(left + self.cell - self.small, top + delta)

    def draw_small_cell(self, left, top):
        square = (left, top, self.small, self.small)
        pygame.draw.rect(self.screen, cell_color, square)



    def draw_borders(self, board: Board.Board):
        columns = board.get_columns()
        rows = board.get_rows()

        width = columns * self.cell
        height = rows * self.cell

        for col in range(0, columns + 1):
            top = self.y0
            bottom = self.y0 + height
            xx = self.x0 + self.cell * col
            pygame.draw.line(self.screen, border_color, (xx, top), (xx, bottom))

        for row in range(0, rows + 1):
            yy = self.y0 + self.cell * row
            pygame.draw.line(self.screen, border_color, (self.x0, yy), (self.x0 + width, yy))
