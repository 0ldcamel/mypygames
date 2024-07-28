import pygame, sys, time


pygame.init()

music_obj = pygame.mixer.music.load('ambient.mp3')
pygame.mixer.music.play(-1, 0.0)
for i in range(60):
    print(i)
    time.sleep(1)