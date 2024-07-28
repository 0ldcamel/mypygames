import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOW_W = 640
WINDOW_H = 480
REVEALSPEED = 8
BOXSIZE = 40
GAP = 10
BOARD_W = 10
BOARD_H = 7

X_MARGIN = int((WINDOW_W - (BOARD_W * (BOXSIZE + GAP))) / 2)
Y_MARGIN = int((WINDOW_H - (BOARD_H * (BOXSIZE + GAP))) / 2)

