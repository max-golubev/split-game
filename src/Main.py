import pygame
import Board
from BoardPainter import *
from BigCell import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
font = pygame.font.Font(None, 40)
done = False

board = Board.Board(6, 5)
painter = BoardPainter(120, 40, screen, font)

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
                    if board.perform_turn(cell, direction):
                        board.finish_turn()

    screen.fill(pygame.Color("black"))
    painter.draw_board(board)
    pygame.display.flip()


