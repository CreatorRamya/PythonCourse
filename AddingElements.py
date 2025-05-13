import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lesson 33: Basic Game Building Concepts")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)

font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to the Game!", True, (0, 0, 0))

rectangle = pygame.Rect(300, 250, 200, 100)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, GREEN, rectangle)

    screen.blit(text, (250, 100)) 

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
sys.exit()
