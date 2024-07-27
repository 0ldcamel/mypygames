import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock =pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('0ld Camel')

catImg = pygame.image.load('cat.png')
mouseImg = pygame.image.load('mouse.jpg')
mousex = 720
mousey = 520
catx = 10
caty = 10
direction = 'right'

while True:
    DISPLAYSURF.fill('white')

    if direction == 'right':
        catx += 5
        if catx == 680:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 520:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(mouseImg, (mousex, mousey))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    fpsClock.tick(FPS)