import pygame

square1 = pygame.Rect(30, 30, 60, 60)
square2 = pygame.Rect(90, 90, 60, 60)

def get_square_for_point(point):
    x, y = point
    if square1.collidepoint(x, y):
        return square1
    if square2.collidepoint(x, y):
        return square2
    return None


def is_in_rect(rect, point):
    x, y = point
    return rect.left <= x <= rect.right and rect.top <= y <= rect.bottom


blue = (0, 0, 255)
red = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1300, 600))

done = False
is_blue = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if square2.collidepoint(mouse_x, mouse_y):
                is_blue = not is_blue
                # print("Mouse x : %d, mouse y: %d" % (mouse_x, mouse_y))
                # print(event.button)
        if event.type == pygame.QUIT:
            done = True

    if is_blue:
        color = blue
    else:
        color = red

    pygame.draw.rect(screen, color, square1)
    pygame.draw.rect(screen, color, square2)

    pygame.display.flip()
