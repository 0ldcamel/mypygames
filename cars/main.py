import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
frame_per_sec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render("Game Over", True, 'black')

background = pygame.image.load('AnimatedStreet.png')

CANVAS = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CANVAS.fill('white')
pygame.display.set_caption("0ld Camel's Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = random.randint(40, SCREEN_WIDTH - 40) , 0
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
enemies.add(E1)
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1, 0.0)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    CANVAS.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, 'black')
    CANVAS.blit(scores, (10, 10))
    score = font.render("Score " + str(SCORE), True, 'blue')

    for entity in all_sprites:
        CANVAS.blit(entity.image, entity.rect)
        entity.move()
        
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        CANVAS.fill('red')
        CANVAS.blit(game_over, (30, 250))
        CANVAS.blit(score, (60, 400))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(5)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    frame_per_sec.tick(FPS)