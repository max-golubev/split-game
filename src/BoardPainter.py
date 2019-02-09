import Board
import BigCell
import pygame

border_color = (0, 0, 255)


class BoardPainter:
    def __init__(self, cell, small, screen: pygame.Surface):
        self.cell = cell #size in pixels
        self.small = small #pixels
        self.screen = screen
        self.x0, self.y0 = 10, 10

    def draw_board(self, board: Board.Board):

        self.draw_borders(board)
        self.draw_cells(board)

    def draw_cells(self, board: Board.Board):
        for row in range(0, board.get_rows()):
            for col in range(0, board.get_columns()):
                cell = board.get_cell(col, row)
                self.draw_cell(cell)

    def draw_cell(self, cell: BigCell.BigCell):
        return

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
