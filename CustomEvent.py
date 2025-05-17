import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event - Circle Sprite Color Change")

clock = pygame.time.Clock()

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000) 

class CircleSprite(pygame.sprite.Sprite):
    def __init__(self, pos, radius):
        super().__init__()
        self.radius = radius
        diameter = radius * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA) 
        self.color = self.random_color()
        self.rect = self.image.get_rect(center=pos)
        self.draw_circle()

    def random_color(self):
        return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def draw_circle(self):
        self.image.fill((0, 0, 0, 0))  
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def change_color(self):
        self.color = self.random_color()
        self.draw_circle()

circle1 = CircleSprite((200, 200), 50)
circle2 = CircleSprite((400, 200), 50)

sprites = pygame.sprite.Group(circle1, circle2)

running = True
while running:
    screen.fill((30, 30, 30)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == CHANGE_COLOR_EVENT:
            for sprite in sprites:
                sprite.change_color()

    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
