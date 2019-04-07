import pygame
import Board
from BoardPainter import *
from BigCell import *

def compute_next_owner(cell: BigCell, direction: Direction):
    owner = cell.get_cell_owner(direction)
    if owner == NOONE:
        return PLAYER_1
    if owner == PLAYER_1:
        return PLAYER_2
    if owner == PLAYER_2:
        return PLAYER_3
    if owner == PLAYER_3:
        return PLAYER_4
    if owner == PLAYER_4:
        return NOONE
    raise "Unknown player: " + repr(owner)


pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False

board = Board.Board(6, 5)
painter = BoardPainter(120, 40, screen)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            cell, direction = painter.find_position(mouse_x, mouse_y, board)
            if cell is not None:
                print("you clicked [%d, %d]" % (cell.get_x(), cell.get_y()) + ", dir: " + repr(direction))
                if direction != Direction.OUTSIDE:
                    next_owner = compute_next_owner(cell, direction)
                    cell.set_cell_owner(direction, next_owner)


    painter.draw_board(board)
    pygame.display.flip()


