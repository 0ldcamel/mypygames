import pygame, sys, random
from pygame.locals import *

pygame.init()

FPS = 30
DISPLAY_W = 800
DISPLAY_H = 600
fpsClock =pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((DISPLAY_W, DISPLAY_H), 0, 32)
pygame.display.set_caption('0ld Camel')

catImg = pygame.image.load('cat.png')
mouseImg_r = pygame.image.load('mouse.jpg')
mouseImg_l = pygame.image.load('mouse_l.png')
mouseRect = mouseImg_l.get_rect()
# mousex = DISPLAY_W - mouseRect[2] - 10
# mousey = DISPLAY_H - mouseRect[3] - 10
mousex = random.randint(10, DISPLAY_W - 10)
mousey = random.randint(10, DISPLAY_H - 10)
catx = 10
caty = 10
direction = 'right'

mouse_dir = [random.randint(0, 5), random.randint(0, 5)]

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
    
    mousex += mouse_dir[0]
    mousey += mouse_dir[1]
    mouseImg = mouseImg_r
    
    if mousex < 10:
        mouse_dir[0] = random.randint(3, 7)
        mouseImg = mouseImg_r
    elif mousex + mouseRect.right > DISPLAY_W - 10:
        mouse_dir[0] = -random.randint(3, 7)
        mouseImg = mouseImg_r

    elif mousey < 10:
        mouse_dir[1] = random.randint(3, 7)
    elif mousey + mouseRect.bottom > DISPLAY_H - 10:
        mouse_dir[1] = -random.randint(3, 7)

    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(mouseImg, (mousex, mousey))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    fpsClock.tick(FPS)