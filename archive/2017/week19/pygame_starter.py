import pygame, sys

from pygame.locals import *


# some constants
FPS = 30 # frames per second setting
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# setup
pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('My First PyGame')

# game objects
player_image = pygame.image.load('octocat.png')
x = SCREEN_WIDTH // 2 - player_image.get_width() // 2
y = SCREEN_HEIGHT // 2 - player_image.get_height() // 2
dx = 0
dy = 0

while True: # the main game loop
    # reset surface
    surface.fill(WHITE)

    # handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                dx = 5
            if event.key == K_DOWN:
                dy = 5
            if event.key == K_LEFT:
                dx = -5
            if event.key == K_UP:
                dy = -5
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                dx = 0
            if event.key == K_DOWN:
                dy = 0
            if event.key == K_LEFT:
                dx = 0
            if event.key == K_UP:
                dy = 0

    x += dx
    y += dy

    # draw objects
    surface.blit(player_image, (x, y))

    # render on screen
    pygame.display.update()

    clock.tick(FPS)