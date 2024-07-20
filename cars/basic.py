import pygame

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("0ld Camel's game")
clock = pygame.time.Clock()
running = True
dt = 1

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.circle(screen, 'red', player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    

    pygame.display.flip()
    dt = clock.tick(60) /1000


pygame.quit()