import pygame

pygame.init()
screen = pygame.display.set_mode((500, 400))
done = False
BLUE = (0, 0, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (220, 20,60 ), pygame.Rect(70, 70, 50, 50))
    pygame.draw.circle(screen, BLUE, (190, 255), 50)
    pygame.draw.circle(screen, BLUE, (144, 255), 50, 3)

    pygame.display.flip()