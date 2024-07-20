import pygame
import time, os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.display.set_caption("0ld Camel's game")

clock = pygame.time.Clock()

pygame.init()
size = 640, 480
window = pygame.display.set_mode(size)
x = 120
y = 120
running = True
while running:
    event_list = pygame.event.get()
    time.sleep(0.1)
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            elif event.key == pygame.K_RIGHT:
                x += 8
            elif event.key == pygame.K_LEFT:
                x -= 8
            elif event.key == pygame.K_DOWN:
                y += 8
            elif event.key == pygame.K_UP:
                y -= 8

    window.fill((0, 0, 0))
    pygame.draw.rect(window, 'blue', (x, y, 400, 240), width=4, border_radius=15)
    pygame.draw.polygon(window, 'red', ((x + 100, y + 10), (x + 160, y + 10), (2 * x + 40, 2 * y + 20), (x * 0.5 + 10, y * 0.5 + 400)), width=10)
    pygame.draw.circle(window, 'yellow', (x * 2 + 100, y * 2 + 50), 100, width=20)
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
