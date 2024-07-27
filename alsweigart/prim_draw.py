import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('0ld Camel')

DISPLAYSURF.fill('white')
pygame.draw.polygon(DISPLAYSURF, 'green', ((146, 0), (291, 106), (236, 277), (56, 277), (90, 106)))
pygame.draw.line(DISPLAYSURF, 'blue', (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, 'blue', (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, 'blue', (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, 'blue', (300, 150), 120, 10)
pygame.draw.circle(DISPLAYSURF, 'red', (300, 150), 60, 5)
pygame.draw.ellipse(DISPLAYSURF, 'red', (300, 250, 120, 80), 1)
pygame.draw.rect(DISPLAYSURF, 'yellow', (200, 150, 100, 50))

BLACK = (0, 0, 0)
RED = (255, 0, 0)

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = RED
del pixObj
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()