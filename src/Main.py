import pygame
import Board
import BoardPainter

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False

board = Board.Board(6, 5)
painter = BoardPainter.BoardPainter(120, 40)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    painter.draw_board(board, screen)
    pygame.display.flip()


