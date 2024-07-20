import pygame, sys
from pygame.locals import * 
pygame.init()
size = 640, 480
window = pygame.display.set_mode(size)
fps = pygame.time.Clock()
fps.tick(60)

car_1 = pygame.Rect((20, 50), (50, 100))
car_2 = pygame.Rect((10, 10), (100, 100))
print('collide =',car_1.collidepoint(50, 75))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()