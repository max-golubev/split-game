
import Board
from BigCell import *
import pygame

border_color = (0, 0, 255)
cell_color = (100, 100, 100)
player_color_1 = (255, 0, 0)
player_color_2 = (0, 255, 0)
player_color_3 = (0, 0, 255)
player_color_4 = (255, 255, 0)

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

    def draw_cell(self, cell: BigCell, col, row):
        for dir in Direction:
            if cell.has_small_cell(dir):
                square = self.get_small_square(cell, dir)
                color = self.get_color(cell, dir)
                pygame.draw.rect(self.screen, color, square)

    def get_color(self, cell: BigCell, dir: Direction):
        owner = cell.get_cell_owner(dir)
        return self.get_color_for_player(owner)

    def get_color_for_player(self, player):
        if player == PLAYER_1:
            return player_color_1
        if player == PLAYER_2:
            return player_color_2
        if player == PLAYER_3:
            return player_color_3
        if player == PLAYER_4:
            return player_color_4
        return cell_color

    def get_small_square(self, cell: BigCell, direction: Direction) -> pygame.Rect:
        top = self.cell * cell.get_y() + self.y0
        left = self.cell * cell.get_x() + self.x0
        delta = (self.cell - self.small) / 2
        if direction == Direction.TOP:
            return (left + delta, top, self.small, self.small)
        if direction == Direction.RIGHT:
            return (left + self.cell - self.small, top + delta, self.small, self.small)
        if direction == Direction.BOTTOM:
            return (left + delta, top + self.cell - self.small, self.small, self.small)
        if direction == Direction.LEFT:
            return (left, top + delta, self.small, self.small)
        return None


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


    def find_position(self, mouse_x, mouse_y, board: Board.Board):
        column = (mouse_x - self.x0) // self.cell
        row = (mouse_y - self.y0) // self.cell
        if column >= board.get_columns() or row >= board.get_rows():
            return None, Direction.OUTSIDE

        cell = board.get_cell(column, row)

        for dir in Direction:
            if not cell.has_small_cell(dir):
                continue
            square = pygame.Rect(self.get_small_square(cell, dir))
            if square.collidepoint(mouse_x, mouse_y):
                return cell, dir
        return cell, Direction.OUTSIDE
