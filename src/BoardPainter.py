import Board
import pygame

border_color = (0, 0, 255)

class BoardPainter:
    def __init__(self, cell, small):
        self.cell = cell
        self.small = small

    def draw_board(self, board: Board.Board, screen: pygame.Surface):
        x0, y0 = 10, 10
        self.draw_borders(x0, y0, board, screen)

    def draw_borders(self, x0, y0, board: Board.Board, screen: pygame.Surface):
        columns = board.get_columns()
        rows = board.get_rows()

        width = columns * self.cell
        height = rows * self.cell

        for col in range(0, columns + 1):
            top = y0
            bottom = y0 + height
            xx = x0 + self.cell * col
            pygame.draw.line(screen, border_color, (xx, top), (xx, bottom))

        for row in range(0, rows + 1):
            yy = y0 + self.cell * row
            pygame.draw.line(screen, border_color, (x0, yy), (x0 + width, yy))


