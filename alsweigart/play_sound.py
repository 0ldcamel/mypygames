import pygame, sys, time


pygame.init()

soundObj = pygame.mixer.Sound('beeps.wav')
for i in range(3):
    soundObj.play()
    time.sleep(1)
    soundObj.stop()