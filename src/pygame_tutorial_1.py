import pygame

blue = (0, 0, 255)
red = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))

done = False
is_blue = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

        if event.type == pygame.QUIT:
            done = True

    if is_blue:
        color = blue
    else:
        color = red

    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.rect(screen, color, pygame.Rect(90, 90, 60, 60))

    pygame.display.flip()
